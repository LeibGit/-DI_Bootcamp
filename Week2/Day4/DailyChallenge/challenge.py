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
    
class TextModification(Text):
    def __init__(self, data):
        super().__init__(data)
        pass

if __name__=="__main__":
    test =  Text("Hello This Is Hello.")
    print(test.word_frequency("Hello"))
    print(test.most_common_word())
    print(test.unique_words())