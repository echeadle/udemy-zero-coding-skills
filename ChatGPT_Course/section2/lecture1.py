import os
import re

def capitalize_sentences(text):
    # Regex to match sentence boundaries
    sentence_endings = re.compile(r'(?<=[.!?]) +')
    sentences = sentence_endings.split(text)
    capitalized_sentences = [s.capitalize() for s in sentences]
    return ' '.join(capitalized_sentences)

def process_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            capitalized_content = capitalize_sentences(content)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(capitalized_content)
            print(f"Processed file: {filename}")

folder_path = 'files'
process_files(folder_path)
