

def in_txt(input: list|dict, file_name: str='') -> IO:
    
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


