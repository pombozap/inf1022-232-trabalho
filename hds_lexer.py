from ply import lex

class HDS_Lexer ():
    def __init__(self):
        self.lexer = lex.lex(module=self)
        self.lexer.begin('INITIAL')

    ### PALAVRAS RESERVADAS ###
    reserved = {
        'RECEBA' : 'RECEBA',
        'DEVOLVA' : 'DEVOLVA',
        'HORADOSHOW' : 'HORADOSHOW',
        'AQUIACABOU' : 'AQUIACABOU',
        'ENQUANTO' : 'ENQUANTO',
        'FACA' : 'FACA',
        'FIM' : 'FIM',
        'SE' : 'SE',
        'SENAO' : 'SENAO',
        'ENTAO' : 'ENTAO',
        'ZERO' : 'ZERO',
        'EXECUTE' : 'EXECUTE',
        'VEZES' : 'VEZES',
        'FIMEXE' : 'FIMEXE',
        'ZERO' : 'ZERO',
    }

    ### TERMINAIS ###
    tokens = ('VARNAME','IGUAL','VIRGULA', 'LPAR', 'RPAR', 'NUM', 'OPARIT', 'OPLOG') + tuple(reserved.values())

    t_ignore = ' \t\n'

    def t_VARNAME(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value,'VARNAME')
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
        print("Invalid Token:",t.value[0])
        t.lexer.skip( 1 )
