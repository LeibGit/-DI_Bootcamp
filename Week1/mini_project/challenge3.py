# challenge 1
def sort_words():
    get_text =  input("Input a string of words(seperate by comma): ")
    text_splt = sorted(get_text.split(','))
    for i in text_splt:
        print(i)
sort_words()

# challenge 2
def longest_str():
    get_text = input("Enter a sentence: ")
    lst_of_text = get_text.replace(',', '').replace('.', '').replace("'", "").replace('?', '').split()
    longest_name =  max(lst_of_text, key=len)
    print(longest_name)
longest_str()