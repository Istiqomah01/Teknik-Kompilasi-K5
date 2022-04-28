from sly import Parser

import coba_lexer

class BasicParser(Parser):
    tokens = coba_lexer.BasicLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
        ('right', UMINUS),
        )

    def __init__(self):
        self.names = { }

    @_('')
    def statement(self, p):
        pass

    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    @_('NAME ASSIGN expr')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.expr)
    
    @_('FOR var_assign TO expr THEN statement')
    def statement(self, p):
        return ('for_loop', ('for_loop_setup', p.var_assign, p.expr), p.statement)

    @_('expr')
    def statement(self, p):
        return (p.expr)

    @_('expr PLUS expr')
    def expr(self, p):
        return ('add', p.expr0, p.expr1)

    @_('expr MINUS expr')
    def expr(self, p):
        return ('sub', p.expr0, p.expr1)

    @_('expr TIMES expr')
    def expr(self, p):
        return ('mul', p.expr0, p.expr1)

    @_('expr DIVIDE expr')
    def expr(self, p):
        return ('div', p.expr0, p.expr1)

    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        return p.expr

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)

    @_('NAME')
    def expr(self, p):
        try:
            return ('var', p.NAME)
        except LookupError:
            print(f'Undefined name {p.NAME!r}')
            return 0

if __name__ == '__main__':
    lexer = coba_lexer.BasicLexer()
    parser = BasicParser()
    env = {}
    while True:
        try:
            text = input('amazone > ')
        except EOFError:
            break
        if text:
            parser.parse(lexer.tokenize(text))
