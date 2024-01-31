from bs4 import BeautifulSoup
import requests as re

# Return hrefs as well if href==TRUE
def get_table_content(src: bool =False) -> list:
   hrefs = []
   ko_words = []
   try:
       req = re.get(src)
       content = BeautifulSoup(req.content, 'html.parser')

       if content.body.table:
           table = content.body.table
           table_dl = table.find('dl').find_all('dd')


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
       for i, j in hrefs and ko_words: 
           full_info = input(src + '\n' + f'HREFS => {i}' + '\n' + f'Words : {j}' + '\n')

       return full_info
   else:
       return ko_words
       



