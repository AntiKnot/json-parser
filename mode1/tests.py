from mode1.lexer import Lexer
from mode1.parser import Parser
from mode1.token import TokenType

if __name__ == '__main__':
    s = '{"foo":"bar","apple":"","pitch":1}'
    le = Lexer(s)
    le.lex()
    p = Parser(le)
    p.parse()
    print(p.lexer.tokens)
    assert p.lexer.tokens[0].value == TokenType.OpenBrace
    print([(token.jtype, token.value) for token in p.lexer.tokens])
