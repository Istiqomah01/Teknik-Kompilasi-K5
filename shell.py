import coba_lexer
import coba_parser
import coba_interpreter

from sys import *

if __name__ == '__main__':
    lexer = coba_lexer.BasicLexer()
    parser = coba_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('amazone > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            coba_interpreter.BasicExecute(tree, env)
