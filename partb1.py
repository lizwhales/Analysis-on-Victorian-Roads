## Part B Task 1

import re
import os
import sys
import csv


def get_document_id(filename):
    # Returns the document_id of an individual document. 

    f = open(filename, "r")
    for line in f.readlines():
        regex = r"[a-zA-Z]{4}\-\d\d\d[a-zA-Z]?"
        match = re.search(regex, line)
        if match != None:
            f.close()
    
            return match.group(0)

    return None

# command line input of 1 arg

if __name__ == "__main__":
    csv_file = "default.csv"
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    else:
        print("[-] Missing output csv file argument")
        sys.exit()

# writes to csv file        
        
    csv_content = [['filename', 'document_id']]
    FOLDER_NAME = "cricket"
    all_files = [os.path.join(FOLDER_NAME, f) for f in os.listdir(FOLDER_NAME)]
    for f in all_files:
        _id = get_document_id(f)
        print(_id)
        if _id != None:
            csv_content.append([f, _id])

    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        for content in csv_content:
            writer.writerow(content)
