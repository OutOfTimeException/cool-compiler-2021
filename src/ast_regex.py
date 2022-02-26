from enum import Enum, auto
from automaton_class import Automaton
from state_class import State
from token_class import Token

import string
from abc import ABC, abstractmethod
from dataclasses import dataclass
from itertools import chain

INVALID = {"", ""}
RESERVED = set(iter(".*+?()[-]^\\"))
ALPHABET = set(iter(string.printable)) - INVALID - set(iter("\n\r\t"))
DIGIT = set(iter(string.digits))
NONDIGIT = ALPHABET - DIGIT

def any_escaper(left: Token |None, right: Token |None):
    if left.lexeme == "." and right.lexeme == "." or left.lexeme =="\\" and right.lexeme != ".":
        lex = right.lexeme
        res= DIGIT if lex=="d" else NONDIGIT if lex=="D" else ALPHABET
        return res
    return {right.lexeme}


def transitions_appender(chars):
    res = Automaton()
    state = State()
    final = State(final=True)
    res.add_state(state)
    res.add_state(final)
    for char in chars:
        state[char] = final
    return res


class TOKEN_TYPE(Enum):
    ALT = auto()
    STAR = auto()
    PLUS = auto()
    MINUS = auto()
    ASK = auto()
    ESC = auto()
    DOT = auto()
    ACC = auto()
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    CHAR=auto()


@dataclass
class Node(ABC):
    @abstractmethod
    def _shift(self):
        pass


class BinaryNode(Node, ABC):
    def __init__(self,left:Node | Token, right:Node | Token):
        self.left:Node | Token=left
        self.right:Node | Token=right


class UnaryNode(Node, ABC):
    def __init__(self,left:Node|Token):
        self.left=left

# A | B
class UnionNode(BinaryNode):
    def __init__(self, left: Node | Token, right: Node | Token):
        super().__init__(left, right)

    def _shift(self):
        left = self.left._shift()
        right = self.right._shift()
        return left | right

# A + B
class ConcatenationNode(BinaryNode):
    def __init__(self, left: Node | Token, right: Node | Token):
        super().__init__(left, right)

    def _shift(self):
        left = self.left._shift()
        right = self.right._shift()
        return left + right

#s* 0-many times
class ClousureStarNode(UnaryNode):
    def __init__(self, left: Node | Token):
        super().__init__(left)

    def _shift(self):
        left = self.left._shift()
        res = left.upd_stars()
        return res.upd_finals()

#s+ at least one time
class ClousurePlusNode(UnaryNode):
    def __init__(self, left: Node | Token):
        super().__init__(left)

    def _shift(self):
        left = self.left._shift()
        left0 = left.copy()
        left1 = left.copy()
        r = left1.upd_stars()
        res = left0 + r
        return res.upd_finals()


#s? 0-1 times
class ClousureMayNode(UnaryNode):
    def __init__(self, left: Node | Token):
        super().__init__(left)

    def _shift(self):
        left = self.left._shift()
        return left.upd_stars()

#(c)
class GrouperNode(UnaryNode):
    def __init__(self, left: Node | Token):
        super().__init__(left)

    def _shift(self):
        return self.left._shift()

#[ElemSet]
class SetterNode(UnaryNode):
    def __init__(self, left: Node | Token):
        super().__init__(left)

    def _shift(self):
        rang=self.left._shift()
        return transitions_appender(rang)

#[^ ElemSet]
class NoSetterNode(UnaryNode):
    def __init__(self, left: Node | Token):
        super().__init__(left)

    def _shift(self):
        alphabet = ALPHABET - self.left._shift()
        return transitions_appender(alphabet)

# . or \
class AnyEscaperNode(BinaryNode):
    def __init__(self, left: Node | Token, right: Node | Token):
        super().__init__(left, right)

    def _shift(self):
        return transitions_appender(any_escaper(self.left,self.right))

# May be a . \ or token 
class ElemSetComNode(BinaryNode):
    def __init__(self, left: Node | Token, right: Node | Token):
        super().__init__(left, right)

    def _shift(self):
        left=any_escaper(self.left.left,self.left.right) if isinstance(self.left , AnyEscaperNode) else None
        left=self.left.lexeme if isinstance(self.left , Token) else left

        right=any_escaper(self.right.left,self.right.right) if isinstance(self.right , AnyEscaperNode) else None
        right=self.right.lexeme if isinstance(self.right , Token) else right

        f_left = self.left._shift() if left is None else left
        f_right = self.right._shift() if right is None else right
        return set(chain(f_left, f_right))

#[a-c] abc
class RangeNode(BinaryNode):
    def __init__(self, left: Node | Token, right: Node | Token):
        super().__init__(left, right)

    def _shift(self):
        left = self.left.lexeme
        right = self.right.lexeme
        if ord(left) > ord(right):
            raise Exception("Invalid Input Range Order")
        chars = [chr(x) for x in range(ord(left), ord(right) + 1)]
        return set(chars)

# a Token Char needs to be converted into a automaton to have a way to be _shifted 
class CharNode(UnaryNode):
    def __init__(self, left: Node | Token):
        super().__init__(left)

    def _shift(self):
        tag = self.left.lexeme
        return transitions_appender([tag])
