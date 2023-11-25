from ply import yacc
from hds_lexer import *
import re

class HDS_Parser ():
    def __init__(self):
        self.parser = yacc.yacc(module=self)
        self.lexer = HDS_Lexer()
        self.error = None

    tokens = HDS_Lexer.tokens

    ### REGRAS GRAMATICAIS ###
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

    def p_val_variavel (self, p):
        'val : VARNAME'
        p[0] = p[1]

    def p_val_numero (self, p):
        'val : NUM'
        p[0] = p[1]
        
    def p_val_parenteses (self, p):
        'val : LPAR val RPAR'
        p[0] = '(%s)'%(p[2])
        
    def p_val_aritmetica (self, p):
        'val : val OPARIT val'
        p[0] = '%s %s %s'%(p[1], p[2], p[3])
        
    def p_condicao_valor (self, p):
        'cond : val'
        p[0] = p[1] + ' > 0'

    def p_condicao_logica (self, p):
        'cond : val OPLOG val'
        p[0] = '%s %s %s'%(p[1], p[2], p[3])

    def p_cmd_while_loop (self, p):
        'cmd : ENQUANTO cond FACA cmds FIM'
        p[0] = 'while %s:{\n%s}\n'%(p[2], p[4])

    def p_cmd_if_then (self, p):
        'cmd : SE cond ENTAO cmds'
        p[0] = 'if %s:{\n%s}\n'%(p[2], p[4])

    def p_cmd_if_then_else (self, p):
        'cmd : SE cond ENTAO cmds SENAO cmds'
        p[0] = 'if %s:{\n%s}\nelse:{\n%s}\n'%(p[2], p[4], p[6])

    def p_cmds_for_loop (self, p):
        'cmd : EXECUTE NUM VEZES cmds FIMEXE'
        p[0] = 'for EXECUTE in range(%s):{\n%s}\n'%(p[2], p[4]) # usa palavra reservada EXECUTE para garantir que não sobrescreve nenhuma variável

    def p_cmd_zero (self, p):
        'cmd : ZERO LPAR VARNAME RPAR'
        p[0] = '%s = 0\n'%(p[3])

    def p_cmd_atribuicao (self, p):
        'cmd : VARNAME IGUAL val'
        p[0] = '%s = %s\n'%(p[1], p[3])

    ### TRATAMENTO DE ERRO ###
    def p_error(self, p):
        self.error = p

    ### GERAÇÃO DE CÓDIGO PYTHON ###
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
    
    ### FUNÇÃO FINAL ###
    def parse(self, codigo_show):
        codigo_python_sem_indentacao = self.parser.parse(codigo_show)

        if self.error != None:
            linhas = codigo_show.splitlines()
            pos_problema = self.error.lexpos
            
            for line in linhas[:self.error.lineno-1]:
                pos_problema -= len(line) + 1

            print("""
            +------------------------------------+
            | %s |
            |                                    |
            | %-34s |
            | %-34s |
            |                                    |
            |         TRADUÇÃO ABORTADA.         |
            +------------------------------------+
            """%(("ERRO DE FORMATAÇÃO NA LINHA %d:"%self.error.lineno).center(34), linhas[self.error.lineno-1], ' ' * pos_problema + '^' * len(self.error.value)))
            return None
            
        else:
            return self.gera_indentacao(codigo_python_sem_indentacao)

