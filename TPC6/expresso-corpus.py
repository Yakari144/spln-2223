#!/usr/bin/env python3
import newspaper
import os

def append_to_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text)

path=os.getcwd()

#if not os.path.exists('/tmp/.newspaper_scrapper'):
#    origem = os.path.join(path,'newspaper_scrapper')
#    os.symlink(origem,'/tmp/.newspaper_scrapper')
url = 'https://expresso.pt/'

jn = newspaper.build(url)                                                                                                                      

print(jn.size())

for article in jn.articles:
    
    ar = newspaper.Article(article.url)
    ar.download()
    ar.parse()
    
    ar.publish_date = ar.publish_date.strftime("%Y_%m_%d")
    if not os.path.exists(f"{path}/artigos/{ar.publish_date}"):
        os.makedirs(f"{path}/artigos/{ar.publish_date}")
    append_to_file(f'{path}/artigos/{ar.publish_date}/{ar.title}.xml',f'''
<article>
    <title>{ar.title}</title>
    <url>{article.url}</url>
    <autor>{ar.authors}</autor>
    <data>{ar.publish_date}</data>
    <text>{ar.text}</text>
</article>
    ''')