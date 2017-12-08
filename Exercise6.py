"""
Exercise 6 from Udemy Python course. This script merges all text files
in current directory into one file and renames it with the current datetime.
"""

import datetime
import glob

file_lst = glob.glob('./*.txt')

filename = datetime.datetime.now()

with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
    for files_ in file_lst:
        with open(files_,'r') as f:
            file.write(f.read()+"\n")

            #f.seek(0)
            #content = f.read()
            #file.write(content+ "\n")
