import string
import time

path = (r'C:\Users\zhang\PycharmProjects\five\text.txt')
with open(path, 'r', encoding='UTF-8') as text:
    words = []
    for raw_word in text.read().split():
        wordss=raw_word.strip(string.punctuation)
        word=wordss.lower()
        words.append(word)
    print(words)
#    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    print(words_index)
    counts_dict={}
    for index in words_index:
        counts_dict[index] =words.count(index)
    print(counts_dict)
    for word in sorted:
        sorted(counts_dict.items(), key=lambda x: x[1], reverse=True)
    print('{}--{} times'.format(word, counts_dict[word]))
#    counts_dict = {index: words.count(index) for index in words_index}
#for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
#    time.sleep(2)
#    print('{}--{} times'.format(word, counts_dict[word]))
