# Part B Task 2
import sys
import re
import os

''' 
- take away non alpha chars
- converts spacing to single whitespace
- change all upper to lowercase
'''


def do_preprocessing(data):
    
    not_to_remove = [' ', '\t', '\n']
    to_convert = not_to_remove[1:]

    buffer = ""
    for _char in data:
        if _char.isalpha() or _char in not_to_remove:
            if _char in to_convert:
                _char = " "
            buffer += _char.lower()
    
    return buffer


# command line arguments = 1

if __name__ == "__main__":
    FOLDER_NAME = "cricket"
    if len(sys.argv) > 1:
        filename = os.path.join(FOLDER_NAME, sys.argv[1])
        with open(filename, "r") as f:
            data = f.read()
        refined_data = do_preprocessing(data)
        print(refined_data)
    else:
        print("[-] Not enough arguments")
