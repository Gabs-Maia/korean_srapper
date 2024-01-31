from urllib.parse import urljoin


def absolute_url(absolute_url):
    url_relatives = ko_words()
    url_absolutes = []    

    for rel in url_relatives:
        absolute = urljoin(KOREAN_ABSOLUTE, rel)
        url_absolutes.append(absolute)
    
    print(url_absolutes)
    return url_absolutes


def relative_url(): 
    
    url_absolute = 