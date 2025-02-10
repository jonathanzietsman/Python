from pathlib import Path

cats = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page200\cats.txt')
dogs = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page200\dogs.txt')
# Write a program that tries to read these files and print the contents
open_cats = open(cats)
open_dogs = open(dogs)

# Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing.
try:
    print(f'\nCats: \n{open_cats.read()}')
    print(f'\nDogs: \n{open_dogs.read()}')
except FileNotFoundError:
    print('One of these files is missing')
    

