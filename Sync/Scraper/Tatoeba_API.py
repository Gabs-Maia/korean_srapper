import requests
import pandas as pd
import os

URL = f"https://api.dev.tatoeba.org/unstable/sentences?lang=eng&q=example&trans=kor&include_unapproved=yes"

def api_test() -> bool:
    try:
        with requests.get(url, timeout=5) as response:
            response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Request Error:{err}")
        return False
    except Exception as err:
        print(f"An unexpected error ocurred: {err}")
        return False
    else: 
        print(f'Success! The status is {response.status_code}')
        return True

def get_sentences(word: str):   
    url = f"https://api.dev.tatoeba.org/unstable/sentences?lang=eng&q={word}&trans=kor&include_unapproved=yes"
    response = requests.get(url)
    
    try:
        data = response.json()['data']
        sentences = []

        for sentence in data:
            id = sentence['id']
            language = sentence['lang']
            phrase = sentence['text']

            for translation in sentence['translations']:
                id_translation = sentence['id']
                translation = sentence['text']                

                sentence_data ={
                    'id': id,
                    'Translations ID': id_translation,
                    'Language' : language,
                    'Sentence' : phrase,
                    'Translation' : translation
                }
                sentences.append(sentence_data)     

        return sentences       

    except Exception as ex:
        print(f'Error when fetching data: {ex}')
        return None 


def transform_to_csv(data: dict, filename: str):
    if not isinstance(data, dict):
        raise ValueError("Data should be a dictionary.")
    
    data_frame = pd.DataFrame(data)
    if os.path.exists(filename):
        print(f"Warning: '{filename}' already exists and will be overwritten.")

        try:
            data_frame.to_csv(filename, index=False)
            print(f"'{filename}' has been written successfully.")
        except Exception as e:
            print(f"An error ocurred while writing to '{filename}' : {str(e)}")


def print_sentences():
    query = 'this'
    sentences = get_sentences(query)
    for sentence in sentences:
        if sentences:
            print(f'{sentence}\n')
        else:
            break 

print_sentences()