from ply import lex

class HDS_Lexer ():
    def __init__(self):
        self.lexer = lex.lex(module=self)
        self.lexer.begin('INITIAL')

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

    def t_VARNAME(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value,'VARNAME')
        return t
    
    def t_IGUAL(self, t):
        r'='
        return t
    
    def t_VIRGULA(self, t):
        r','
        return t

    def t_error(self, t):
        print("Invalid Token:",t.value[0])
        t.lexer.skip( 1 )
