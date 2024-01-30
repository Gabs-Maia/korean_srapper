from deep_translator import GoogleTranslator as gl
from bs4 import BeautifulSoup
import requests as re
from urllib.parse import urljoin

KOREAN_ABSOLUTE = "https://en.wiktionary.org"
KOREAN_FREQUENCY = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800"
HREFS = []
KO_WORDS = []

# Return HREFS as well if href==TRUE
def korean_words(links=False, src=False):
   try:
       req = re.get(KOREAN_FREQUENCY)
       content = BeautifulSoup(req.content, 'html.parser')

       if content.body.table:
           table = content.body.table
           table_dl = table.find('dl').find_all('dd')


           for href in table_dl:
               link = href.find('a')['href']
               ko_word = href.text
               KO_WORDS.append(ko_word)
               HREFS.append(link)               
       else:
           print('No tables were found in the body!')
           return None
    
   except Exception as ex:
       print(f'An error has occurred: {ex}')
       return None
   
   if src:
       for i, j in HREFS and KO_WORDS: 
           full_info = print(KOREAN_FREQUENCY + '\n' + f'HREFS => {i}' + '\n' + f'Words : {j}' + '\n')
           print(full_info)

       return full_info
   
   if links==False:
        return KO_WORDS
   else:
       return KO_WORDS, HREFS

def transform_to_txt():
    input = korean_words()
    stringed_input = str(input).strip()
    try:
        with open('korean.txt', 'w', encoding='utf-8') as file:
           written = file.write(stringed_input)   
           return written        
    
    except Exception as e:
        print("There is a Problem", str(e))

def bulk_translation():
    
    for i, d


def translate_file():
    with open('korean1.txt', 'r', encoding='utf-8') as eng_translation:
        file_translation = eng_translation.read()
    eng_txt = str(gl(source='ko', target='en').translate(file_translation))
    with open('korean_eng.txt', 'w', encoding='utf-8') as to_file:
        to_file.write(eng_txt)
    return to_file


def split_file():
    with open('korean.txt', 'r', encoding='utf-8') as file:
        words = file.read().split()

    division = len(words) // 4
    chunks = [words[i:i+division] for i in range(0, len(words), division)]

    for i, chunk in enumerate(chunks, start=1):
        with open(f'korean{i}.txt', 'w', encoding='utf-8') as file:
            file.write(' '.join(chunk))



