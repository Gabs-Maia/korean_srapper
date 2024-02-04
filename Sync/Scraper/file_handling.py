import os
import shutil
from Sync.links import SUBDIRS_LANGUAGES, TEXT_DIR_PATH

def prepare_context(base_dir: str, names: list) -> None:
    os.makedirs(base_dir, exist_ok=True)

    for name in names:
        sub_dir = os.path.join(base_dir, name)
        os.mkdir(sub_dir)

        file_path = os.path.join(sub_dir, f'{name}.txt')
        with open(file_path, 'w') as file:
            pass

    prepare_context(sub_dir, [])


def to_txt(input: list|dict, file_name: str='') -> IO:
    
    stringed_input = str(input).strip()
    try:
        with open(f'{file_name}.txt', 'w', encoding='utf-8') as file:
           file.write(stringed_input)          
    
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

