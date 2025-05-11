# Import Path class to handle file paths in a cross-platform way
from pathlib import Path

# Control flag for the input loop - program runs while this is True
active = True

# List to store visitor names during the current session
current = []

# Main input loop - keeps asking for names until 'quit' is entered
while active:
    # Get visitor's name from user input
    user = input('Enter your Name: ')
   
    # Check if user wants to quit
    if user == 'quit':
        active = False  # Stop the loop if 'quit' is entered
    else:
        # Add the name to our current session list if not quitting
        current.append(user)

# Display all names collected in this session
print(current)

# Create a Path object pointing to our guest book file
# Using raw string (r) to handle Windows file paths correctly
path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page192\guest_book.txt')

# Open the file in append mode ('a') to add new names without erasing existing ones
with open(path, 'a') as file:
    # Write each collected name to the file
    # Adding '\n' after each name puts each visitor on a new line
    for name in current:
        file.write(name + '\n')
        