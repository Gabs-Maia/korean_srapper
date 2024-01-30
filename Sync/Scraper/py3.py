

def absolute_url(absolute_url):
    url_relatives = ko_words()
    url_absolutes = []    

    for rel in url_relatives:
        absolute = urljoin(KOREAN_ABSOLUTE, rel)
        url_absolutes.append(absolute)
    
    print(url_absolutes)
    return url_absolutes


def translate_phrase():
    
    translate = korean_words()
    string_list = str(translate)
    text = re.sub('[,\[\]]', '', string_list) 
    google = GoogleTranslator(source='ko', targeg='en').translate(string_list)      
    splited = text.split()

    return text
