from typing import List

from token_class import Token, tokenizer
from match_class import Match
from serializer_class import Serializer

class LexerTable(list, Serializer):
    def __init__(self, ignore, eof, eoline):
        super(LexerTable, self).__init__()
        self.ignore = ignore
        self.eof = eof
        self.eoline = eoline

class Lexer:
    def __init__(self,match:Match,token_type=None):
        if token_type:
            globals()["TOKEN_TYPE"] = token_type
        
        self.table:LexerTable = LexerTable.deserializer("{Wp48S^xk9=GL@E0stWa761SMbT8$j-~l55p<Mt#0S<2ALUnt`F?cWKUXM8oLhSG;hOd5zCzR$MhZ)7XF<1oE>>H!KryvmM-HDo+>qV%K@m%>Ww3+^=<NFokPf=3i42c+fek7Klg`)ALvCv2}_;6$PYC3Shjhdz>>k!R>>j1>MO*D>8iK#T(V!f!KqmKI{nXPKNT-&jH;IW#Y{BaoF+gni<h`uDBMhE(>xMPy&8G-W7`lx*100000@|i1_ZaY&600F%Lqyhi{`lsxfvBYQl0ssI200dcD")
        self.match:Match=match
        for t in self.table:
            if t[0] != self.table.eof:
                self.match.add_matcher(t)
        self.match.initialize()

    def __call__(self,input:str) ->List[Token]:
        token_list= tokenizer(input,self.table.ignore,self.table.eof,self.table.eoline,self.match)
        return token_list
