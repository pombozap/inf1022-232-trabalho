from ply import lex

tokens = (
    'receba',
    'devolva',
    'horadoshow',
    'aquiacabou',
    'enquanto',
    'faca',
    'fim',
    'igual',
    'virgula',
    'varname',
)

t_ignore = ' \t'

t_receba = r'RECEBA'
t_devolva = r'DEVOLVA'
t_horadoshow = r'HORADOSHOW'
t_aquiacabou = r'AQUIACABOU'
t_enquanto = r'ENQUANTO'
t_faca = r'FACA'
t_fim = r'FIM'
t_igual = r'='
t_virgula = r','
t_varname = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_error( t ):
    print("Invalid Token:",t.value[0])
    t.lexer.skip( 1 )

lexer = lex.lex()

import ply.yacc as yacc

#precedence = (
#    ( 'left', 'PLUS', 'MINUS' ),
#    ( 'left', 'TIMES', 'DIV' ),
#    ( 'nonassoc', 'UMINUS' )
#)

def p_1 (p):
    'program : receba varlist devolva varlist horadoshow cmds aquiacabou'
    p[0] = """
    def func (%s):\n
    {\n
    %s
    return %s\n
    }\n
    """%(p[2], p[6], p[4])

def p_2 (p):
    'varlist : varname virgula varlist'
    p[0] = p[1] + ', ' + p[3]

def p_3 (p):
    'varlist : varname'
    p[0] = p[1]

def p_4 (p):
    'cmds : cmd cmds'
    p[0] = p[1] + p[2]

def p_5 (p):
    'cmds : cmd'
    p[0] = p[1]

def p_6 (p):
    'cmd : enquanto varname faca cmds fim'
    p[0] = """
    while %s != 0:\n
    {\n
    %s
    }\n
    """%(p[2], p[4])

def p_7 (p):
    'cmd : varname igual varname'
    p[0] = '%s = %s\n'

def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()

input_file = open("test.show", "r")
res = parser.parse(input_file.read()) # the input
input_file.close()
output_file = open("horadoshow.py", "w")
output_file.write(res)
output_file.close()
print(res)