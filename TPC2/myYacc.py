import ply.yacc as yacc
from myLex import tokens,literals

def p_1(p):
    "dic : Es"
    p[0] = p[1]
    print(p[1])

def p_2(p):
    "Es : E LINHA_B Es"
    p[0] = p[1] + p[2] + p[3]

def p_3(p):
    "Es : E"
    p[0] = p[1]

def p_4(p):
    "E : Itens"
    p[0] = p[1]

def p_5(p):
    "Itens : Item ',' Itens"
    p[0] = p[1] + p[2] + p[3]

def p_6(p):
    "Itens : Item"
    p[0] = p[1]

def p_7(p):
    "Item : AtrC"
    p[0] = p[1]

def p_8(p):
    "Item : Ling"
    p[0] = p[1]

def p_9(p):
    "AtrC : ID ':' VALOR"
    p[0] = p[1] + p[2] + p[3]

def p_10(p):
    "Ling : IDL ':' Ts"
    p[0] = p[1] + p[2] + p[3]

def p_11(p):
    "Ts : Ts ';' T"
    p[0] = p[1] + p[2] + p[3]

def p_12(p):
    "Ts : T"
    p[0] = p[1]

def p_13(p):
    "T : '-' VALOR AtrTs"
    p[0] = p[1] + p[2] + p[3]

def p_14(p):
    "AtrTs : AtrTs2"
    p[0] = p[1]

def p_15(p):
    "AtrTs : "
    p[0] = ""

def p_16(p):
    "AtrTs2 : AtrTs2 AtrT"
    p[0] = p[1] +  p[2]

def p_17(p):
    "AtrTs2 : AtrT"
    p[0] = p[1]

def p_19(p):
    "AtrT : '+' ID ':' VALOR"
    p[0] = p[1] + p[2] + p[3] + p[4]


def p_error(p):
    print('Erro sintático: ',p)
    parser.sucess = False

parser = yacc.yacc()
parser.sucess = True
f = open("exemplo.txt","r")
program = f.read()

parser.parse(program)
if parser.sucess:
    print("Programa bem estruturado")
else:
    print("Programa Inválido")