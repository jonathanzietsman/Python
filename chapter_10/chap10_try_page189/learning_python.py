from pathlib import Path

path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page189\learning_python.txt')

open_file = open(path)

contents = open_file.read()

print(contents)

list = open_file.readlines()

for item in list:
    print(item)

