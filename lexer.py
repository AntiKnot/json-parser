from errors import CharMissError
from errors import ValidTypeError
from token import Token
from token import TokenType


class Lexer:
    # space = re.compile('[\s]+')
    # number = re.compile('[\d]+')

    def __init__(self, s):
        self.s = s
        self.pos = 0
        self.pmax = len(s) - 1
        self.curr_char = self.s[self.pos]
        self.tokens = []
        self.currentTokenIndex = 0

    def lex(self):
        while self.curr_char and (self.curr_char != TokenType.EOF):
            self.skip_white_space()
            if self.curr_char == "{":
                self.consume()
                token = Token(TokenType.OpenBrace, TokenType.OpenBrace)
            elif self.curr_char == "}":
                self.consume()
                token = Token(TokenType.CloseBrace, TokenType.CloseBrace)
            elif self.curr_char == ":":
                self.consume()
                token = Token(TokenType.COLON, TokenType.COLON)
            elif self.curr_char == ",":
                self.consume()
                token = Token(TokenType.COMMA, TokenType.COMMA)
            elif self.curr_char == '"':
                token = self.get_string_token()
            else:
                if self.is_number(self.curr_char):
                    token = self.get_number_token()
                else:
                    raise ValidTypeError
            if token:
                self.tokens.append(token)
        self.tokens.append(Token(TokenType.EOF, TokenType.EOF))

    def skip_white_space(self):
        while (not self.is_end()) and self.is_space(self.curr_char):
            self.consume()

    def consume(self):
        if not self.is_end():
            self.pos += 1
            self.curr_char = self.s[self.pos]
        else:
            self.curr_char = TokenType.EOF

    def match(self, input_char):
        if self.curr_char == input_char:
            self.consume()
        else:
            raise CharMissError

    def is_end(self):
        return self.pos >= self.pmax

    def is_space(self, char):
        return char == ' '
        # return self.space.match(char)

    def is_number(self, char):
        return char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # return self.number.match(char)

    def get_string_token(self):
        buffer = ""
        self.match(TokenType.QUOTE.value)
        while self.curr_char != TokenType.QUOTE.value and not self.is_end():
            buffer += self.curr_char
            self.consume()
        self.match(TokenType.QUOTE.value)
        if buffer:
            # self.tokens.append(Token(TokenType.StringLiteral, buffer))
            return Token(TokenType.StringLiteral, buffer)

    def get_number_token(self):
        buffer = ""
        while self.is_number(self.curr_char) and not self.is_end():
            buffer += self.curr_char
            self.consume()
        if buffer:
            return Token(TokenType.NUMBER, buffer)

    def get_next_token(self):
        if self.currentTokenIndex <= len(self.tokens) - 1:
            res = self.tokens[self.currentTokenIndex]
            self.currentTokenIndex += 1
            return res
        return
