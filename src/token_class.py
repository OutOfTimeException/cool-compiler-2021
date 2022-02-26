from match_class import Match

class Token:
    def __init__(self,id,line:int,column:int,lexeme:str,type=None):
        self.id: str=id
        self.line: int=line
        self.column: int=column
        self.lexeme: str=lexeme
        self.type: str=type

    def __str__(self):
        return f"Token {self.id}, line {self.line}, column {self.column}"

    def __repr__(self):
        return f"Token {self.id}, line {self.line}, column {self.column}"

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return hash(self) == hash(other)

def tokenizer(input:str,ignore:str,eof:str,eoline:str,match:Match):
    tokens = []
    pos = 0
    line = column = 1
    l = len(input)
    while pos < l:
        token = input[pos]
        if token == eoline:
            line += 1
            column = 0
        elif token == ignore:
            column += 1
        id, lexeme, type = match.match(input, pos)
        if not lexeme:
            raise ValueError(f"Lexicographic Error '{token}' at line: {line} column: {column}")
        token= Token(id, line, column, lexeme,type)
        lexeme_len = len(lexeme)
        pos += lexeme_len
        column += lexeme_len
        if not type:
            tokens.append(token)
    eof = Token(eof,line,column, eof, "")
    tokens.append(eof)
    return tokens