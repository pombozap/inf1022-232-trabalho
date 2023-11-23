from ply import lex

class MyLexer:
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

    def t_VARNAME(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value,'VARNAME')
        return t

    def t_error( t ):
        print("Invalid Token:",t.value[0])
        t.lexer.skip( 1 )

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
