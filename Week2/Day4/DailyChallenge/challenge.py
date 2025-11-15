import string
import nltk
from nltk.corpus import stopwords
import re

nltk.download('stopwords')
class Text():
    def __init__(self, text: str):
        self.text = text

    def word_frequency(self, word: str):
        split_list = self.text.split()
        for word in split_list:
            count = split_list.count(word)
            if count == 0:
                return None
        return count
    
    def most_common_word(self):
        clean_list = self.text.replace('.', '').replace(',', '')
        split_list = clean_list.split()
        word_freq = {}
        for word in split_list:
            if word in word_freq:
                word_freq[word] = word_freq[word] + 1
            else:
                word_freq[word] = 1 
        max_key_value =  max(word_freq, key=word_freq.get)
        return max_key_value

    def unique_words(self):
        word_set = set()
        clean_list = self.text.replace('.', '').replace(',', '')
        split_list = clean_list.split()
        for word in split_list:
            if word in word_set:
                continue
            else:
                word_set.add(word)
        return list(word_set)
    
    def form_file(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content

class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)
    
    def remove_punctuation(self):
        punctuation_chars = string.punctuation
        print(punctuation_chars)
        for char in punctuation_chars:
            if char in self.text:
                new_str = self.text.replace(f'{char}', '')
        return new_str

    def remove_stop_words(self):
        stop_words = list(stopwords.words('english'))
        for word in stop_words:
            if word in self.text:
                new_text = self.text.replace(f'{word}', '')
        return new_text
    
    def remove_special_chars(self):
        special_chars = re.findall(r'[^a-zA-Z0-9\s]', self.text)
        for char in special_chars:
            if char in self.text:
                new_text = self.text.replace(f'{char}', '')
        return new_text

if __name__=="__main__":
    test =  Text("Hello This Is Hello.")
    test2 = TextModification("Hello This Is Hello.")
    print(test.word_frequency("Hello"))
    print(test.most_common_word())
    print(test.unique_words())
    print(test.form_file(r"C:\Users\leibn\Downloads\random_words.txt"))
    print(test2.remove_punctuation())
    print(test2.remove_stop_words())
    print(test2.remove_special_chars())