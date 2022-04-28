from sly import Lexer
 
class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, PLUS, TIMES, MINUS, DIVIDE, ASSIGN, LPAREN, RPAREN, FOR, TO, THEN}
    ignore = '\t '

    # Define tokens
    FOR = r'untuk'
    TO = r's/d'
    THEN = r'ulang'
    NUMBER = r'\d+'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
   

    # Simbol matematika
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'
    


    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'//.*')
    def COMMENT(self, t):
        pass
    
    # action for newlines
    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')


    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

if __name__ == '__main__':
    lexer = BasicLexer()
    env = {}
    while True:
        try:
            text = input('amazone > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
