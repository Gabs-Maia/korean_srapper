#The only APIs that are free...
from deep_translator import (GoogleTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator)
from py2 import korean_words


def translate_phrase():
    
    translate = korean_words()
    trans_list = []

    for word in translate:
        google = GoogleTranslator(source='ko', targeg='en').translate(word)
        trans_list.append(google)
    
    print(trans_list)
    return

translate_phrase()
    









        

        

        

    



