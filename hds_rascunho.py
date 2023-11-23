from ply import lex
import ply.yacc as yacc

reserved = {
    'RECEBA' : 'RECEBA',
    'DEVOLVA' : 'DEVOLVA',
    'HORADOSHOW' : 'HORADOSHOW',
    'AQUIACABOU' : 'AQUIACABOU',
    'ENQUANTO' : 'ENQUANTO',
    'FACA' : 'FACA',
    'FIM' : 'FIM',
}

tokens = ('VARNAME','IGUAL','VIRGULA') + tuple(reserved.values())

t_ignore = ' \t\n'
t_IGUAL = r'='
t_VIRGULA = ','

def t_VARNAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'VARNAME')
    return t

def t_error( t ):
    print("Invalid Token:",t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_programa (p):
    'expr : RECEBA varlist DEVOLVA varlist HORADOSHOW cmds AQUIACABOU'
    p[0] = 'def func(%s):{\n%s\nreturn %s}\n'%(p[2], p[6], p[4])

def p_variavel_unica (p):
    'varlist : VARNAME'
    p[0] = p[1]

def p_varias_variaveis (p):
    'varlist : VARNAME VIRGULA varlist'
    p[0] = '%s, %s'%(p[1], p[3])

def p_comando_unico (p):    # newlines considerados em cada cmd
    'cmds : cmd'
    p[0] = p[1]

def p_varios_comandos (p):  # newlines considerados em cada cmd
    'cmds : cmd cmds'
    p[0] = p[1] + p[2]

def p_cmd_while_loop (p):
    'cmd : ENQUANTO VARNAME FACA cmds FIM'
    p[0] = 'while %s > 0:{\n%s}\n'%(p[2], p[4])

def p_cmd_atribuicao (p):
    'cmd : VARNAME IGUAL VARNAME'
    p[0] = '%s = %s\n'%(p[1], p[3])

def p_erro(p):
    print("Erro de sintaxe no input!")

parser = yacc.yacc()

input_file = open("input.show", "r")
read = input_file.read()
input_file.close()

res = parser.parse(read) # the input

def conserta_newlines (s):
    print(s)
    final = ''
    indent_atual = 0
    for c in s:
        if c == '{':
            indent_atual += 1
        elif c == '}':
            indent_atual -= 1
        elif c == '\n':
            final = final + '\n' + indent_atual * '\t'
        else:
            final = final + c

    return final

res = conserta_newlines(res)
print(res)

output_file = open("horadoshow.py", "w")
output_file.write(res)
output_file.close()
