#!/usr/bin/env python3
import newspaper
import os

path=os.getcwd()

if not os.path.exists('/tmp/.newspaper_scrapper'):
    origem = os.path.join(path,'newspaper_scrapper')
    os.symlink(origem,'/tmp/.newspaper_scrapper')
url = 'https://www.jn.pt'

jn = newspaper.build(url)                                                                                                                      

print(jn.size())

for article in jn.articles:
    print(article.url, article.title)
    ar = newspaper.Article(article.url)
    ar.download()
    ar.parse()
    print(f'''
<article>
    <title>{ar.title}</title>
    <url>{article.url}</url>
    <autor>{ar.authors}</autor>
    <data>{ar.publish_date}</data>
    <text>{ar.text}</text>
</article>
    ''')