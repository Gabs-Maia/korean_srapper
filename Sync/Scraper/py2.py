from bs4 import BeautifulSoup
import requests as re
from urllib.parse import urljoin

KOREAN_ABSOLUTE = "https://en.wiktionary.org"
KOREAN_FREQUENCY = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800"

# Return hrefs as well if href==TRUE
def korean_words(links=False, src=False):
   try:
       req = re.get(KOREAN_FREQUENCY)
       content = BeautifulSoup(req.content, 'html.parser')

       if content.body.table:
           table = content.body.table
           table_dl = table.find('dl').find_all('dd')

           hrefs = []
           ko_words = [] 

           for href in table_dl:
               link = href.find('a')['href']
               ko_word = href.text
               ko_words.append(ko_word)
               hrefs.append(link)               
       else:
           print('No tables were found in the body!')
           return None
    
   except Exception as ex:
       print(f'An error has occurred: {ex}')
       return None
   
   if src:
       full_info = print(KOREAN_ABSOLUTE + '\n' + f'hrefs => {hrefs}' + '\n' + f'Words : {ko_words}' + '\n')
       return full_info
   
   if links==False:
        return ko_words
   else:
       return ko_words, hrefs
       



