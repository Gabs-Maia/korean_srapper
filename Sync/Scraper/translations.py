#The only APIs that are free...
from deep_translator import (GoogleTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator)
from Sync.Scraper.content_scraper import korean_words

#This only works for file name formated  as {language}{i}.txt
def translate_textTXT(i: int, language: str,source: str, target: str, number_of_parts: int) -> None:
    if i > number_of_parts:
        return 
    else:    
        with open(f'{language}{i}.txt', 'r+', encoding='utf-8') as f:
            file = f.read()
            translation_to = str(GoogleTranslator(source=source, target=target).translate(file))
            f.seek
            f.write(translation_to)

        translate_text(i+1, number_of_parts)

    
def compare_translationsTXT(i: int, language: str, source: str, target: str) -> str:
    
   try:
       with open(f'{language}{i}.txt', 'r+', encoding='utf-8') as file:
           content = file.read()
           translators = [
                GoogleTranslator(source=source, target=target),
                PonsTranslator(source=source, target=target),
                LingueeTranslator(source=source, target=target),
                MyMemoryTranslator(source=source, target=target),
           ]
           
           text = str(translator.translate_file(content))
           translations = [text for translator in translators]
           file_structure = f'{translator.__class__.__name__} : {translation} \n'
           structure = [file_structure for translator, translation in zip(translators, translations)]
           file.write(structure)
           return ''.join(translations)
   except Exception as ex:
       print(f'An error has occured: {ex}')
       return None
   
