## Part B Task 4
import sys
import os
import csv
from nltk.stem import PorterStemmer
from partb2 import do_preprocessing
from partb3 import csv_to_dict, is_keyword_present


# looks for keywords

ps = PorterStemmer()
keywords = []
if len(sys.argv) > 1:
    keywords = sys.argv[1:]
else:
    print("[-] Please enter keywords to look for")

# checks for inexact matching with stemmer    
    
temp = []
for word in keywords:
    temp.append(word)
    word_stem = ps.stem(word)
    if word_stem != word:
        temp.append(word_stem)

keywords = temp
del temp

register = csv_to_dict("partb1.csv")
for _file in register.keys():
    with open(_file) as f:
        data = f.read()
    data = do_preprocessing(data)
    for word in keywords:
        if is_keyword_present(data, word):
            print("{} : {}".format(word, register[_file]))
