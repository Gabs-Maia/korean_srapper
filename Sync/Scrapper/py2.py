from bs4 import BeautifulSoup
import requests as re

def ko_hrefs():
    url = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800"
    req = re.get(url)
    content = BeautifulSoup(req.content, 'html.parser')
    table = content.body.table
    table_dl = table.find('dl').find_all('dd')

    hrefs = []

    for href in table_dl:
        href = href.find('a')['href']
        hrefs.append(href)
    
    return hrefs

      

ko_hrefs()
