from pathlib import Path

path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page192\guest.txt')

user_name = input('Enter your name: ')

with path.open(mode='a') as file:
    file.write(user_name + '\n')

print('Done! ')
