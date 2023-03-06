import ply.lex as lex

literals = [':', '-', '+',',',';']

tokens = ['ID', 'IDL', 'VALOR', 'LINHA_B']

def t_IDL(t):
    r'(es)|(en)|(pt)|(la)|(ga)'
    #print("IDL: ",t)
    return t

def t_ID(t):
    r'\w+'
    #print("ID: ",t)
    return t

def t_LINHA_B(t):
    r'--'
    #print("NL: ",t)
    return t

def t_VALOR(t):
    r'"[^"\n]*"'
    #print("VALOR: ",t)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ANY_ignore = " \t\n"
    
lexer = lex.lex()