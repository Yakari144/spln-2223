import requests
from bs4 import BeautifulSoup

def betclic(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    odds = []
    teams = []

    for div in soup.find_all('span', class_='oddValue'):
        odd = div.text.strip().replace('\n','')
        odds.append(odd)

    for div in soup.find_all('span', class_='oddMatchName'):
        team = div.text.strip().replace('\n','')
        teams.append(team)

    for i in range(len(odds)):
        if i in range(len(teams)):
            print(str(i) + ": " + teams[i] + " - " + odds[i])

def betclic2():
    url = 'https://www.betclic.pt/futebol-s1'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    hrefs = []
    for a in soup.find_all('a', href=True):
        if "/futebol-s1/" in a['href']:
            # from a url like https://www.betclic.pt/futebol-s1/inglaterra-premier-league-1/arsenal-vs-chelsea-1 get https://www.betclic.pt/futebol-s1/inglaterra-premier-league-1
            href = a['href'].split('/')
            href = "https://www.betclic.pt/"+href[1]+"/"+href[2]+"/"
            if href not in hrefs:
                hrefs.append(href)
    for href in hrefs:
        print(href)
        betclic(href)


def bet22():
    url = "https://22bet-bet.com/pt/line"
    response = requests.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    odds = []
    teams = []

    for div in soup.find_all("span", class_="c-bets__inner"):
        odd = div.text.strip().replace('\n','')
        odds.append(odd)

    for div in soup.find_all("span", class_="c-events__team u-ovh"):
        team = div.text.strip().replace('\n','')
        teams.append(team)

    for i in range(len(odds)):
        print(str(i) + ": " + teams[i] + " - " + odds[i])


betclic2()

#betclic('https://www.betclic.pt/futebol-s1')