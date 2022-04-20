#CONSTANTA
from distutils.log import error
from lib2to3.pgen2 import token


DIGITS = '0123456789'
ABJAD = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# PESAN ERROR 
class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result
class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Karakter tidak diketahui', details)

# INISIALISASI TOKEN
TT_INT='INT'
TT_FLOAT='FLOAT'
TT_PLUS='TAMBAH'
TT_MINUS='KURANG'
TT_MUL='KALI'
TT_DIV='BAGI'
TT_LPAREN='KURUNG BUKA'
TT_RPAREN='KURUNG TUTUP'
TT_CABD='KAREKTER ABJAD'

class Token:
    def __init__(self,type_,value=None):
        self.type=type_
        self.value=value
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

# INI BAGIAN LEXER
class Lexer:
    def __init__(self, text):
        self.text=text
        self.pos=-1
        self.current_char=None
        self.advance()

    def advance(self):
        self.pos +=1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []
        while self.current_char !=None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char in ABJAD:
                tokens.append(self.make_abc())

            elif self.current_char =='+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char =='-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char =='*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char =='/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char =='(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char ==')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                char = self.current_char
                self.advance()
                return[], IllegalCharError("'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str=''
        dot_count=0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1 : break
                dot_count += 1
                num_str +='.'
            else:
                num_str += self.current_char
            self.advance()
        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))
            
    def make_abc(self):
        num_abc=''
        dot_abc=0

        while self.current_char != None and self.current_char in ABJAD:
            if self.current_char == '/t':
                if dot_abc == 1 : break
                dot_abc += 1
                num_abc +='/t'
            else:
                num_abc += self.current_char
            self.advance()
            return Token(TT_CABD,num_abc)

# Menjalankan (RUN) File

def Run(text):
    lexer= Lexer(text)
    token, error = lexer.make_tokens()

    return token, error