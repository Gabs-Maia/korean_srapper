from deep_translator import GoogleTranslator as gl
from bs4 import BeautifulSoup
import requests as re
from urllib.parse import urljoin
from typing import IO

def bulk_in_txt(input: list|dict, file_name: str='') -> IO:
    
    stringed_input = str(input).strip()
    try:
        with open(f'{file_name}.txt', 'w', encoding='utf-8') as file:
           written = file.write(stringed_input)          
    
    except Exception as e:
        print("There is a Problem", str(e))

def split_file(language: str, parts: int = 4):
    with open(f'{language}.txt', 'r', encoding='utf-8') as file:
        words = file.read().split()

    division = len(words) // parts
    chunks = [words[i:i+division] for i in range(0, len(words), division)]

    for i, chunk in enumerate(chunks, start=1):
        with open(f'{language}{i}.txt', 'w', encoding='utf-8') as file:
            file.write(' '.join(chunk))

def bulk_translation(i: int, language: str,source: str, target: str, number_of_parts: int) -> None:
    if i > number_of_parts:
        return 
    else:    
        with open(f'{language}{i}.txt', 'r+', encoding='utf-8') as f:
            file = f.read()
            translation_to = str(gl(source=source, target=target).translate(file))
            f.seek
            f.write(translation_to)

        bulk_translation(i+1, number_of_parts)

koWords = korean_words()
bulk_in_txt(koWords,file_name='korean')
split_file('korean', 4)
bulk_translation(1, 'korean', 'ko', 'en', 4)

