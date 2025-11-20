

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



if __name__=="__main__":
    instance_1 = AnagramChecker()
    print(instance_1.is_valid(word="Shakshuka"))