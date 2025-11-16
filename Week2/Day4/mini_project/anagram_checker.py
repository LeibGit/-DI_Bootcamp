import json

def get_words():
    file_path = r"C:\Users\leibn\Downloads\sowpods\sowpods.txt"
    with open(file_path, 'r') as file:
        content = file.read().lower()
        return content
    
class AnagramChecker():
    def __init__(self, word_list=None):
        self.word_list = get_words()
    
    def is_valid(self, word):
        if word in self.word_list:
            return True
        else:
            return False
    @classmethod      
    def is_anagram(self, word1, word2):
        if sorted(word1) == sorted(word2):
            return True
        else:
            return False
    
    def get_anagrams(self, word_to_check):
        anagram_storage = []
        for word in self.word_list.strip().split():
            if self.is_anagram(word, word_to_check):
                anagram_storage.append(word)
            else:
                continue
        return anagram_storage