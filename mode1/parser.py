from mode1.errors import TokenMissError
from mode1.token import Token
from mode1.token import TokenType


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.curr_token: Token = self.lexer.get_next_token()

    def parse(self):
        self.parse_value()

    def parse_value(self):
        if self.curr_token.jtype == TokenType.OpenBrace:
            self.parse_object()
        elif self.curr_token.jtype == TokenType.NUMBER:
            self.parse_number()
        elif self.curr_token.jtype == TokenType.StringLiteral:
            self.parse_string()
        elif self.curr_token.jtype == TokenType.TRUE:
            self.eat(TokenType.TRUE)
        elif self.curr_token.jtype == TokenType.FALSE:
            self.eat(TokenType.FALSE)

    def parse_object(self):
        """
        obj
        : "{" pair (,pair)* "}"
        ;
        """
        self.eat(TokenType.OpenBrace)
        self.parse_pair()
        while self.curr_token.jtype == TokenType.COMMA:
            self.eat(TokenType.COMMA)
            self.parse_pair()
        self.eat(TokenType.CloseBrace)

    def parse_number(self):
        self.eat(TokenType.NUMBER)

    def parse_string(self):
        self.eat(TokenType.StringLiteral)

    def parse_pair(self):
        self.eat(TokenType.StringLiteral)
        self.eat(TokenType.COLON)
        self.parse_value()

    def eat(self, token_type):
        if self.curr_token.jtype == token_type:
            self.curr_token = self.lexer.get_next_token()
        else:
            raise TokenMissError
