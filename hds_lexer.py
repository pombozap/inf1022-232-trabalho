from ply import lex

class HDS_Lexer ():
    def __init__(self):
        self.lexer = lex.lex(module=self)
        self.lexer.begin('INITIAL')

    ### PALAVRAS RESERVADAS ###
    reserved = ('RECEBA',
                'DEVOLVA',
                'HORADOSHOW',
                'AQUIACABOU',
                'ENQUANTO',
                'FACA',
                'FIM',
                'SE',
                'SENAO',
                'ENTAO',
                'ZERO',
                'EXECUTE',
                'VEZES',
                'FIMEXE',
                )

    ### TERMINAIS ###
    tokens = ('VARNAME','IGUAL','VIRGULA', 'LPAR', 'RPAR', 'NUM', 'OPARIT', 'OPLOG', 'NEWLINE') + reserved

    t_ignore = ' ' + '\t'

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_VARNAME(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if t.value in self.reserved:
            t.type = t.value

        return t
    
    t_IGUAL = r'='
    t_VIRGULA = r','
    t_LPAR = r'\('
    t_RPAR = r'\)'
    t_NUM = r'[0-9]+'
    t_OPARIT = r'\+|\*|-|/'
    t_OPLOG = r'>|<|>=|<='

    ### TRATAMENTO DE ERRO ###
    def t_error(self, t):
        print(">>> Caractere inválido lido:",t.value[0])
        t.lexer.skip(1)
