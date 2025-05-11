# Import the Path class from pathlib for handling file paths
from pathlib import Path

# Create a Path object pointing to the guest list file
path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page192\guest.txt')

# Get the user's name through console input
user_name = input('Enter your name: ')

# Open the file in append mode ('a') to add the new name
# The 'with' statement ensures the file is properly closed after writing
with path.open(mode='a') as file:
    # Write the user's name to the file, followed by a newline character
    file.write(user_name + '\n')

# Confirm that the operation is complete
print('Done! ')
