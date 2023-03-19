import ply.yacc as yacc
from myLex import tokens,literals

ats = {}
ts = {}
its = {}
dicionario = {}
count = 0

def p_1(p):
    "dic : Es"
    #print(dicionario)
    pass

def p_2(p):
    "Es : E LINHA_B Es"
    pass

def p_3(p):
    "Es : E"
    pass

def p_4(p):
    "E : Itens"
    global count,its,dicionario
    p[0] = dicionario.update({f'{count}' : its})
    count += 1
    its = {}

def p_5(p):
    "Itens : Item ',' Itens"
    pass

def p_6(p):
    "Itens : Item"
    pass

def p_7(p):
    "Item : AtrC"
    global its
    p[0] = its.update(p[1])

def p_8(p):
    "Item : Ling"
    global its
    p[0] = its.update(p[1])

def p_9(p):
    "AtrC : ID ':' VALOR"
    p[0] = {p[1] : p[3]}

def p_10(p):
    "Ling : IDL ':' Ts"
    global ts
    p[0] = {p[1] : ts}
    ts = {}

def p_11(p):
    "Ts : Ts ';' T"
    p[0] = ts.update(p[3])

def p_12(p):
    "Ts : T"
    p[0] = ts.update(p[1])

def p_13(p):
    "T : '-' VALOR AtrTs"
    global ats
    p[0] = {p[2]: ats}
    ats = {}

def p_14(p):
    "AtrTs : AtrTs2"
    pass

def p_15(p):
    "AtrTs : "
    pass

def p_16(p):
    "AtrTs2 : AtrTs2 AtrT"
    pass

def p_17(p):
    "AtrTs2 : AtrT"
    pass

def p_19(p):
    "AtrT : '+' ID ':' VALOR"
    p[0] = ats.update({p[2] : p[4]})

# function that turns a string with ' to a string with "
    

def p_error(p):
    print('Erro sintático: ',p)
    parser.sucess = False

def header():
    pagWeb = """
<!DOCTYPE html>
<html>
    <head>
        <title>Dicionario Conceptual</title>
        <meta charset="utf-8"/>
    </head>
    <body>"""
    return pagWeb
    
def footer():
    pagWeb = """
    </body>
</html>"""
    return pagWeb

def dictToHTML(dic,i):
    s=""
    for a in dic:
        s += f"<pre>"
        s += f"<h{i+1}>"
        i2 = i
        while i2 > 0:
            s += "     "
            i2 -= 1
        s += a
        if type(dic[a]) == dict: 
            s += f"</h{i+1}></pre>\n"   
            s += dictToHTML(dic[a],i+1)
        else:
            s += " : "
            s += dic[a]
            s += f"</h{i+1}></pre>\n"
    return s

def gerador(dic):
    pagWeb = header()
    pagWeb += dictToHTML(dic,0)
    pagWeb += footer()
    fo = open('output.html','w')
    fo.write(pagWeb)
    fo.close()

parser = yacc.yacc()
parser.sucess = True
f = open("exemplo.txt","r")
program = f.read()

parser.parse(program)
if parser.sucess:
    print("Programa bem estruturado")
    gerador(dicionario)
else:
    print("Programa Inválido")