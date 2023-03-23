#!/usr/bin/evn python3
'''tokenizerSpln'''

import argparse
import re
import fileinput
import os

__version__ = "0.3"

def main():
    
    parser = argparse.ArgumentParser(
                        prog='tok',
                        description='Tokenizador de livros',
                        epilog='')
    parser.add_argument('filename', help="ficheiro de input a ser lido")
    parser.add_argument('-l','--ling',default='pt', help="lingua na qual o livro está escrito")
    args = parser.parse_args()

    # get the current directory
    dirname = os.path.abspath(__file__)
    # remove the file name from the path
    dirname = dirname[:dirname.rfind('/')]
    f_abrev = dirname+'/conf/abrev.txt'

    text=""
    f_input = open(args.filename,'r')
    text = f_input.read()
    f_input.close()

    def removeEmptyAndWhiteSpaceLines(lista):
            return [x.strip() for x in lista if x.strip() != '']

    def load_abrev():
        f = open(f_abrev, 'r')
        txt = f.read()
        lang= txt.split('#')
        lang = removeEmptyAndWhiteSpaceLines(lang)
        abrev = {}
        for l in lang:
            ling,*abrevs = l.split('\n')
            abrevs = removeEmptyAndWhiteSpaceLines(abrevs)
            abrev[ling] = abrevs
        f.close()
        return abrev
    
    def getAbrevRegex(abrevs,ling):
        abrs =  abrevs[ling]
        reg = r'('
        nFirst = False
        for a in abrs:
            if nFirst:
                reg+=r'|'
            reg+=r''+a+r'\.'
            nFirst=True
        reg += r')'
        return reg
        
    abrevs=load_abrev()

    # Tratamento de palavras cujo ponto pertence------
    if args.ling in abrevs:
        regex_abrevs = getAbrevRegex(abrevs,args.ling)
        text = re.sub(regex_abrevs, r'<abrv>\1</abrv>', text, flags=re.IGNORECASE)

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
    ## keywords multilingues
    ## titulo do capitulo na linha seguinte e depois linha em branco
    ## Marcar tambem outras unidades de quebra (prologo, introducao, epilogo, etc)
    regex_cap = r'.*(CAP[ÍI]TULO( )+\w+).*\n(.*)\n'
    text = re.sub(regex_cap, r'\n<endline>## \1 ##\n<endline># \3 #<paragrafo>', text)

    # 3. Marcar paragrafos de linhas pequenas


    # 4. Juntar linhas da mesma frase
    reg_par = r'([.?!§:]”?)(\s*?)\n(?=[^a-z])'
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
    text = re.sub(r'</?abrv>',r'',text)

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

main()
