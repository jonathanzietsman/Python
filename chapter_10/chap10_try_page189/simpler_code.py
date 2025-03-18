# Specify the name of the file to read
filename = r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page189\learning_python.txt'

# Open the file and automatically close it after reading
with open(filename) as file_object:
    # Read the entire content of the file as a single string
    contents = file_object.read()
    
    # Loop directly over each line obtained from splitlines()
    # splitlines() splits the content by line breaks and returns a list of lines
    for line in contents.splitlines():
        # Print each line from the file
        print(line)
