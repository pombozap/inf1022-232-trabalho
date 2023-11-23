from ply import yacc
from hds_lexer import HDS_Lexer

class HDS_Parser(object):

    def __init__(self):

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

        def p_error(p):
            print("Erro de sintaxe no input!")
        self.lexer = HDS_Lexer()
        self.parser = yacc.yacc()

    def parse(self, str):
        return self.parser.parse(str) # the input