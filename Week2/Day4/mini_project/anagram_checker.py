import json

def get_words():
    file_path = r"C:\Users\leibn\Downloads\sowpods\sowpods.txt"
    with open(file_path, 'r') as file:
        content = file.read().lower()
        return content
    
class AnagramChecker():
    def __init__(self, word_list: list):
        self.word_list = get_words()
