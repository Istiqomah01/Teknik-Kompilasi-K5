from sly import Lexer
 
class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, PRINT, STRING, IF, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens
    PRINT = r'cetak'
    IF = r'jika'
    THEN = r'maka'
    ELSE = r'namun_jika'
    FOR = r'untuk'
    FUN = r'fungsi'
    TO = r'ke'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')



if __name__ == '__main__':
    lexer = BasicLexer()
    env = {}
    while True:
        try:
            text = input('lexer > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
