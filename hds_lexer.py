from ply import lex

class HDS_Lexer ():
    def __init__(self):
        self.lexer = lex.lex(module=self)
        self.lexer.begin('INITIAL')
        self.linestart = [0]

    ### PALAVRAS RESERVADAS ###
    reserved = ('RECEBA',
                'DEVOLVA',
                'HORADOSHOW',
                'AQUIACABOU',
                'ENQUANTO',
                'FACA',
                'FIMENQUANTO',
                'SE',
                'SENAO',
                'ENTAO',
                'FIMSE',
                'ZERO',
                'EXECUTE',
                'VEZES',
                'FIMEXE',
                'FIM',
                )

    ### TERMINAIS ###
    tokens = ('VARNAME','IGUAL','VIRGULA', 'LPAR', 'RPAR', 'NUM', 'OPARIT', 'OPLOG', 'OPLOGEQ', 'newline') + reserved

    t_ignore = ' ' + '\t'

    def t_newline(self, t): # Regra ainda ignora newlines, só conta eles para imprimir erro
        r'\n'
        self.linestart.append(t.lexpos + 1)
        t.lexer.lineno += 1

    def t_VARNAME(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if t.value in self.reserved:
            t.type = t.value

        return t
    
    t_OPLOG = r'>|<'
    t_OPLOGEQ = r'>=|<='
    t_IGUAL = r'='
    t_VIRGULA = r','
    t_LPAR = r'\('
    t_RPAR = r'\)'
    t_NUM = r'[0-9]+'
    t_OPARIT = r'\+|\*|-|/'

    ### TRATAMENTO DE ERRO ###
    def t_error(self, t):
        print(">>> AVISO!  Caractere inválido \'%c\' lido na linha %d (col=%d) e considerado como espaço."%(t.value[0], t.lineno, t.lexpos-self.linestart[t.lineno-1]))

        t.lexer.skip(1)
