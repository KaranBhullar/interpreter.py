from enum import Enum, auto
"""
-> tokens class
-> lexemes
-> 

"""
# I think a better representation is using a dictionary
class TokenType(Enum):
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    ADD = auto()
    SUB = auto()
    MUL = auto()
    MOD = auto()
    DIV = auto()
    EOF = auto()
    # EOF = auto()
    # EOF = auto()
    # EOF = auto()
    # EOF = auto()
    # EOF = auto()
    # EOF = auto()
    # EOF = auto()
    # EOF = auto()
    # EOF = auto()
    # EOF = auto()
    # EOF = auto()

# using lookup table for single char tokens and their corresponding values
single_lookup = {
    "(": TokenType.LEFT_PAREN,
    ")": TokenType.RIGHT_PAREN,
    "{": TokenType.LEFT_BRACE,
    "}": TokenType.RIGHT_BRACE,
    "+": TokenType.ADD,
    "-": TokenType.SUB,
    "*": TokenType.MUL,
    "%": TokenType.MOD,
    "/": TokenType.DIV,
    # < ... > will fill the rest in a sec
}

# Probably include object literal in design
class Token:
    def __init__(self, token_type: TokenType, lexeme: str, location: list):
        self.token_type = token_type
        self.lexeme = lexeme
        self.location = location # do I need this (maybe)?


class Scanner:
    def __init__(self, source: str) -> None:
        self.source = source
        self.location = [1, 0]
        self.current = 0
    
    # Main Scanning function
    def scan(self) -> list[Token]:
        # Should split

        # Placeholder
        return [Token(single_lookup["+"], "+", [1,1])]
    
    # Scanning signle token
    def scan_token(self) -> None:
        while (len(self.source) > self.location[1]):
            print(self.source[self.location[1]])
            self.location[1] += 1
        return None
    
    # Char @ current position in self.source
    def next(self):
        return self.source[self.current]
    
    # increments the location of the column in a line
    def inc(self) -> int:
        self.location[1] += 1
        return self.location[1]
