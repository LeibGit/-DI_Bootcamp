

class AnagramChecker():
    file_path = r"C:\Users\leibn\Downloads\sowpods\sowpods.txt"
    
    with open(file_path, 'r') as file:
        file_content = file.read()

    def __init__(self, text_file=file_content):
        self.text_file = text_file.lower()
    
    def __str__(self):
        return f"Text: {self.text_file}"

    def __repr__(self):
        return f"Text: {self.text_file}"
    
    def is_valid(self, word):
        if word.lower() in self.text_file:
            return "Valid"
        else:
            return "word not found"

    def get_anagrams(self, word):
        list_of_anagrams = []
        for w in self.text_file.split():
            if self.is_anagram(word1=word, word2=w) == True:
                list_of_anagrams.append(w)
            else:
                continue
        return list_of_anagrams

    def is_anagram(self, word1, word2):
        sorted1 = sorted(word1)
        sorted2 = sorted(word2)
        if sorted1 == sorted2:
            return True
        else:
            return False