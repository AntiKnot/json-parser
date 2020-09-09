from enum import Enum
from enum import unique


@unique
class TokenType(Enum):
    OpenBrace = "{"
    CloseBrace = "}"
    StringLiteral = "StringLiteral"
    COLON = ":"
    QUOTE = '"'
    NUMBER = "NUMBER"
    COMMA = ","
    NIL = "NIL"
    EOF = "EOF"
    TRUE = "true"
    FALSE = 'false'


# @unique
# class KeyWorks(Enum):
#     true = TokenType.TRUE
#     false = TokenType.FALSE


class Token:
    def __init__(self, jtype, value):
        """
        :param jtype:
        :param value:
        """
        self.jtype = jtype
        self.value = value
