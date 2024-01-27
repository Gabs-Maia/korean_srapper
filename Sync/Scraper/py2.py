from bs4 import BeautifulSoup
import requests as re
from urllib.parse import urljoin

KOREAN_ABSOLUTE = "https://en.wiktionary.org"
KOREAN_FREQUENCY = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800"

# Return hrefs as well if href==TRUE
def ko_words(links=False):
    try:
        KOREAN_FREQUENCY = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800"
        req = re.get(KOREAN_FREQUENCY)
        content = BeautifulSoup(req.content, 'html.parser')
        table = content.body.table
        
        hrefs = []
        ko_words = []

        for href in table_dl:
            link = href.find('a')['href']
            ko_word = href.text
            ko_words.append(ko_word)
            hrefs.append(link)
    
    except Exception as ex:
        print(f'An error has ocurred: {ex} !')
        
           
        
    if links == True :
        return ko_words, hrefs
    else:
        return ko_words
    

print(ko_words())

def absolute_url(KOREAN_ABSOLUTE):
    url_relatives = ko_words()
    url_absolutes = []    

    for rel in url_relatives:
        absolute = urljoin(KOREAN_ABSOLUTE, rel)
        url_absolutes.append(absolute)
    
    print(url_absolutes)
    return url_absolutes

