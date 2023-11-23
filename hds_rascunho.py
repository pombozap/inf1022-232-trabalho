from ply import lex
import ply.yacc as yacc

tokens = (
    'TEST1',
    'TEST2',
    'VARNAME'
)

t_ignore = ' \t\n'

t_TEST1 = r'TEST1'
t_TEST2 = r'TEST2'
t_VARNAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_error( t ):
    print("Invalid Token:",t.value[0])
    t.lexer.skip( 1 )

lexer = lex.lex()

def p_1 (p):
    'expr : TEST1 VARNAME TEST2'
    p[0] = "print(%s)\n"%(p[2])

def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()

input_file = open("test.show", "r")
read = input_file.read()
input_file.close()

res = parser.parse("TEST1 HelloWorld TEST2") # the input

output_file = open("horadoshow.py", "w")
output_file.write(res)
output_file.close()

print(res)