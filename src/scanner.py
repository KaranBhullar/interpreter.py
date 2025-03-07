from enum import Enum, auto
"""
    - Add support for literals
    - Make sure to increment location on \n and inc (I probably won't need logic for col)
"""
# Exception if lexeme is unknown
class UnknownKeyError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)

class TokenType(Enum):
    # Parentheses
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    # Operations
    ADD = auto()
    SUB = auto()
    MUL = auto()
    MOD = auto()
    DIV = auto()
    POW = auto()
    # Literals
    NUMBER = auto()
    STRING = auto()
    BOOLEAN = auto()
    # Misc
    EXMARK = auto()
    DOT = auto()
    COMMA = auto()
    # Equality
    GREATER = auto()
    LESS = auto()
    EQUAL = auto()
    GTEQUAL = auto()
    LTEQUAL = auto()
    EQEQUAL = auto()
    NOTEQUAL = auto()
    # End of File
    EOF = auto()



lookup = {
    # Parentheses
    "(": TokenType.LEFT_PAREN,
    ")": TokenType.RIGHT_PAREN,
    "{": TokenType.LEFT_BRACE,
    "}": TokenType.RIGHT_BRACE,
    # Operations
    "+": TokenType.ADD,
    "-": TokenType.SUB,
    "*": TokenType.MUL,
    "%": TokenType.MOD,
    "/": TokenType.DIV,
    "^": TokenType.POW,
    # Literals
    # Misc
    "!": TokenType.EXMARK,
    ".": TokenType.DOT,
    ",": TokenType.COMMA,
    # Equality
    ">": TokenType.GREATER, # likely not needed
    "<": TokenType.LESS,
    "=": TokenType.EQUAL,
    
}

class Token:
    def __init__(self, token_type: TokenType, lexeme: str, location: list[int], literal=None):
        self.token_type = token_type
        self.lexeme = lexeme
        self.location = location 
        self.literal = literal

    def stringify(self):
        print(f"{self.lexeme} | {self.token_type} | {self.location}")

class Scanner:
    def __init__(self, src: str) -> None:
        self.src = src
        self.start = 0
        self.pos = [1, 1]
        self.curr = 0
        self.tokens: list[Token] = []
    
    def scan(self) -> list:
        print(self.src)
        while (not self.completed()):
            self.match()
        self.add_token(TokenType.EOF, '\0', self.pos, None)
        return self.tokens


    def completed(self):
        if (self.curr >= len(self.src)): return True
        return False
    
    def match(self) -> None:
        self.start = self.curr
        match self.current():
            case '!':
                self.add_token(TokenType.NOTEQUAL, '!=', self.pos, None) if self.next('=') else self.add_token(TokenType.EXMARK, '!', self.pos, None)
            case '>':
                self.add_token(TokenType.GTEQUAL, '>=', self.pos, None) if self.next('=') else self.add_token(TokenType.GREATER, '>', self.pos, None)
            case '<':
                self.add_token(TokenType.LTEQUAL, '<=', self.pos, None) if self.next('=') else self.add_token(TokenType.LTEQUAL, '<', self.pos, None)
            case '=':
                self.add_token(TokenType.EQEQUAL, '==', self.pos, None) if self.next('=') else self.add_token(TokenType.EQUAL, '=', self.pos, None)
            case '/':
                pass
            case '\n':
                self.pos[0] += 1
                self.pos[1] = 0
            case _:
                if self.current() not in lookup: raise UnknownKeyError("An unknown character has occurred")
                self.add_token(lookup[self.current()], self.current(), self.pos) # base case for any single-char lexeme
        self.pos[1] += 1
        self.adv()

    def add_token(self, token_type: TokenType, lexeme: str, pos: list, literal=None) -> None:
        self.tokens.append(Token(token_type, lexeme, pos.copy(), literal)) # error before was that I was passing by reference, not by value

    def current(self) -> str:
        return self.src[self.curr]

    def adv(self) -> None:
        self.curr += 1
        return

    def peek(self) -> str | None:
        if self.completed() or self.curr == len(self.src) - 1: return None
        return self.src[self.curr + 1]
        # return self.src[self.curr + 1] if (not self.completed()) else None

    def next(self, char: str):
        next = True if (self.peek() == char) else False
        if next: self.adv();self.pos[1] +=1
        return next

    # Test function
    def to_str(self):
        for token in self.tokens:
            token.stringify()
