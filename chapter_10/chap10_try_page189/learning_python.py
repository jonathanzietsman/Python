# Import the Path class from pathlib for handling file paths
from pathlib import Path

# Create a Path object pointing to the text file we want to read
path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page189\learning_python.txt')

# Open the file in read mode
open_file = open(path)

# Read the entire contents of the file as a single string
contents = open_file.read()

# Print the entire file contents
print(contents)

# Read all lines from the file into a list
list = open_file.readlines()

# Iterate through each line and print it
for item in list:
    print(item)

