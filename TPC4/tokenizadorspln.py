#!/usr/bin/evn python3

import sys
import re
import fileinput

text=""
for line in fileinput.input():
    text+=line

# Tratamento de palavras cujo ponto pertence
regex_sr = r'(Sr(t?)(a?))\s*(\.)'
text = re.sub(regex_sr, r'<sr>\1\4</sr>', text)

# Tratamento de reticiencias
regex_ret = r'\.\.\.'
text = re.sub(regex_ret,r'§',text)

# 0. Quebra de pagina
regex_pag = r'([a-z0-9,;-])\n\n([a-z0-9])'
text = re.sub(regex_pag, r'\1\n\2', text)

# 1. Separar pontuação das palavras
regex_pAntes = r'(\W)([-–—.:;!?,§])(\w)'
text = re.sub(regex_pAntes, r'\1\2 \3', text, flags=re.UNICODE)
regex_pDepois = r'(\w)([-–—.:;!?,§])( |\n|[-–—.:;!?,§])'
text = re.sub(regex_pDepois, r'\1 \2\3', text, flags=re.UNICODE)

# 2. Marcar capitulos
regex_cap = r'.*(CAP[ÍI]TULO( )+\w+).*\n(.*)\n'
text = re.sub(regex_cap, r'\n<endline>## \1 ##\n<endline># \3 #<paragrafo>', text)

# 3. Marcar paragrafos de linhas pequenas


# 4. Juntar linhas da mesma frase
reg_par = r'([.?!§:]”?)(\s*?)\n'
text = re.sub(reg_par,r'\1\n</paragrafo>\n<paragrafo>',text)

# 5. Uma frase por linha
text = re.sub(r'\n',r' ',text)
reg_frase=r'([.?!§:]”?)\s*([A-Z0-9“–])'
text = re.sub(reg_frase,r'\1<frase>\2',text,flags=re.UNICODE)

# 6. Trata poemas
arr_poemas = []

def guarda_poema(poema):
    arr_poemas.append(poema[1])
    return f">>{len(arr_poemas)}<<"

regex_poema = r'<poema>(.*?)</poema>'
text = re.sub(regex_poema,guarda_poema, text, flags=re.S)

# 7. Trata tags
text = re.sub(r'<endline>',r'\n',text)
text = re.sub(r'<paragrafo>',r'\n\n',text)
text = re.sub(r'</paragrafo>',r'',text)
text = re.sub(r'<frase>',r'\n\t',text)
text = re.sub(r'§','...',text)
text = re.sub(r'</?sr>',r'',text)

## variadas maneiras de identificar paragrafos
# 1. linha em branco
# 2. tag <p>
# 3. indentação no inicio de um paragrafo
# 4. um paragrafo por linha
# 5. quebra de pagina

## Quebra de pagina
# 1. \f
# 2. Nr de pagina
# 3. linha em branco


print(text)


#### TPC

# DEFINIR O TRABALHO PRATICO
# Avancar e por de forma a que aparecesse como ferramenta, 
# como fazer para ficar superferramenta ou seja se o ficheiro viesse do word 
# tambem podia usa-lo(talvez usar um conversor) e arranjarmos ferramentas que 
# ja existam para nos ajudar top. possivel se indique ao utilizdor que tenha 
# que indicar os poemas ou indicar qual o tipo da quebra de pagina, por ex