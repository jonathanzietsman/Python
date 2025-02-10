""" 10-11. Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dumps() to store this number in a file. Write a separate program that reads in this value and prints the message “I know your favorite
number! It’s _____.” """

from pathlib import Path
import json

#! prompts for the user’s favorite number
user_info = input('Favorite Number? ')

path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page206\users_imformation.json')

#!Use json.dumps() to store this number in a file
contents = json.dumps(user_info)
path.write_text(contents)