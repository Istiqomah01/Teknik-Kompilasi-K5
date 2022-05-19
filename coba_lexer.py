from sly import Lexer

class BasicLexer(Lexer):
    print("Selamat Datang di Bahasa Pemrograman Amazone")
    tokens = { NAME, NUMBER, STRING, IF, THEN, FUNCTION, ELSE, FOR, TO, ARROW, EQEQ, PRINT }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' ,'>', '<' }

    # Mendefinisikan Token
    PRINT = r'tampil'
    IF = r'jika'
    THEN = r'ulang'
    ELSE = r'maka'
    FOR = r'untuk'
    FUNCTION = r'fungsi'
    TO = r's/d'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    NUMBER = r'\d+'
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