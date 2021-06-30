## Part B Task 3
import sys
import os
import csv
from partb2 import do_preprocessing


def csv_to_dict(filename):
    # reads the csv file and returns the filename:id dict 

    _dict = {}
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            _dict[row[0]] = row[1]
    del _dict["filename"]

    return _dict

def is_keyword_present(data, keyword):
    # searches the txt file for keyword

    if keyword.lower() in data.split():
            return True
    return False


if __name__ == "__main__":
    keywords = []
    if len(sys.argv) > 1:
        keywords = sys.argv[1:]
    else:
        print("[-] Please enter keywords to look for")

    register = csv_to_dict("partb1.csv")

    for _file in register.keys():
        with open(_file) as f:
            data = f.read()
        data = do_preprocessing(data)

        for word in keywords:
            if is_keyword_present(data, word):
                print("{} : {}".format(word, register[_file]))
            
