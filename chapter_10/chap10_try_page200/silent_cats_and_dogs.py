# Import the Path class from pathlib for handling file paths
from pathlib import Path

# Create Path objects pointing to our cat and dog files
cats = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page200\cats.txt')
dogs = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page200\dogs.txt')

# Open both files for reading
open_cats = open(cats)
open_dogs = open(dogs)

# Use a try-except block to handle potential file reading errors
try:
    # Attempt to read and print the contents of both files
    print(f'\nCats: \n{open_cats.read()}')
    print(f'\nDogs: \n{open_dogs.read()}')
except FileNotFoundError:
    # Silently ignore the error without printing any message
    pass
    
# Properly close both files to free up system resources
open_cats.close()
open_dogs.close()

