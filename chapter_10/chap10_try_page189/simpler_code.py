# This program demonstrates a simpler way to read and process file contents
# using the 'with' statement, which automatically handles file closing

# Specify the full path to the text file we want to read
filename = r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page189\learning_python.txt'

# Use the 'with' statement to open and automatically close the file
# This is a more Pythonic way to handle files as it ensures proper cleanup
with open(filename) as file_object:
    # Read all contents of the file into a single string
    contents = file_object.read()
    
    # Process the file contents line by line

    # splitlines() splits the content by line breaks and returns a list of lines
    # This is more efficient than readlines() for large files
    for line in contents.splitlines():
        # Print each line from the file
        print(line)
