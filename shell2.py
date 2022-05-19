import coba_lexer
import coba_parser
import coba_interpreter

from sys import *

#Di run di terminal dengan program yang telah dibuat
lexer = coba_lexer.BasicLexer()
parser = coba_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    coba_interpreter.BasicExecute(tree, env)