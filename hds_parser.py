from ply import yacc
from hds_lexer import *

class HDS_Parser ():
    def __init__(self):
        self.parser = yacc.yacc(module=self)
        self.lexer = HDS_Lexer()

    tokens = HDS_Lexer.tokens

    def p_programa (self, p):
        'expr : RECEBA varlist DEVOLVA varlist HORADOSHOW cmds AQUIACABOU'
        p[0] = 'def func(%s):{\n%s\nreturn %s}\n'%(p[2], p[6], p[4])

    def p_variavel_unica (self, p):
        'varlist : VARNAME'
        p[0] = p[1]

    def p_varias_variaveis (self, p):
        'varlist : VARNAME VIRGULA varlist'
        p[0] = '%s, %s'%(p[1], p[3])

    def p_comando_unico (self, p):    # newlines considerados em cada cmd
        'cmds : cmd'
        p[0] = p[1]

    def p_varios_comandos (self, p):  # newlines considerados em cada cmd
        'cmds : cmd cmds'
        p[0] = p[1] + p[2]

    def p_cmd_while_loop (self, p):
        'cmd : ENQUANTO VARNAME FACA cmds FIM'
        p[0] = 'while %s > 0:{\n%s}\n'%(p[2], p[4])

    def p_cmd_atribuicao (self, p):
        'cmd : VARNAME IGUAL VARNAME'
        p[0] = '%s = %s\n'%(p[1], p[3])

    def p_error(self, p):
        print("Erro de sintaxe no input!")

    def gera_indentacao (self, codigo_sem_indentacao):
        codigo_python = ''
        indent = 0
        for char in codigo_sem_indentacao:
            match char:
                case '{':
                    indent += 1
                case '}':
                    indent -= 1
                case '\n':
                    codigo_python = codigo_python + '\n' + indent * '\t'
                case _:
                    codigo_python = codigo_python + char
        
        return codigo_python
    
    def parse(self, codigo_show):
        return self.gera_indentacao(self.parser.parse(codigo_show))

