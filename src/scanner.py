from enum import Enum, auto

"""
    - Proper checking for integer and floating point values
    - Should check if next lexeme has decimal and if so the type should be float
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
    INTEGER = auto()
    FLOAT = auto()
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
        # print(f"{ self.lexeme: <10 }|  {self.token_type: ^10}| { self.location : >10}")

        print(f"{self.lexeme : <15}{self.token_type : ^15}{self.location[0] : >15}, { self.location[1]}") 

class Scanner:
    def __init__(self, src: str) -> None:
        self.src = src
        self.start = 0
        self.pos = [1, 1]
        self.curr = 0
        self.tokens: list[Token] = []
    
    def string(self): # <- ignores last character in string (due to peek function)
        lexeme = ''
        self.adv()

        while self.current() != '"':
            lexeme += self.current()
            self.pos[1] += 1

            if not self.peek() and self.current() != '"': 
                raise UnknownKeyError("String not closed")

            self.adv()

        self.add_token(TokenType.STRING, lexeme, self.pos, str)

    def number(self):
        lexeme = ''
        token_type = TokenType.INTEGER

        while self.current().isdigit():
            lexeme += self.current()

            if self.next('.'):
                if '.' in lexeme: raise UnknownKeyError("Invalid float representation")
                token_type = TokenType.FLOAT
                lexeme += self.current()

            if not self.peek() or not self.peek().isdecimal():
                print("done from number")
                break

            self.adv()

        self.add_token(token_type, lexeme, self.pos, int)


    def scan(self) -> list:
        print(self.src) # Temporary

        while (not self.completed()):
            self.match()

        self.add_token(TokenType.EOF, '\0', self.pos, None)
        return self.tokens


    def completed(self):
        if (self.curr >= len(self.src)): return True

        return False
    
    def match(self) -> None:
        self.start = self.curr # <-- May need changing because lexemes are shown at their ending position, not starting position

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
            case '"':
                self.string()
            case _ if self.current().isdecimal():
                self.number()
            case ' ' | '\t' | '\r': # types of whitespace
                pass # Whitespaces should be ignored
            case '\n':
                self.pos[0] += 1
                self.pos[1] = 0
            case _:
                if self.current() not in lookup: raise UnknownKeyError("An unknown character has occurred")
                self.add_token(lookup[self.current()], self.current(), self.pos) # base case for any single-char lexeme

        self.pos[1] += 1
        self.adv()

    def add_token(self, token_type: TokenType, lexeme: str, pos: list, literal=None) -> None:
        self.tokens.append(Token(token_type, lexeme, pos.copy(), literal)) 
        return

    def current(self) -> str:
        return self.src[self.curr]

    def adv(self) -> None:
        self.curr += 1
        return

    def peek(self) -> str | None:
        if self.completed() or self.curr == len(self.src) - 1: return None

        return self.src[self.curr + 1]

    def next(self, char: str):
        next = True if (self.peek() == char) else False
        if next: self.adv();self.pos[1] +=1 # adv and increment the location by 1

        return next

    # Test function
    def to_str(self) -> None:
        for token in self.tokens:
            token.stringify()
        return
