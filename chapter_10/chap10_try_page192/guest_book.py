from pathlib import Path

active = True
current = []
while active:
    user = input('Enter your Name: ')
   
    if user == 'quit':
        active = False
    else:
        current.append(user)

print(current)

path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page192\guest_book.txt')
with open(path, 'a') as file:
    for name in current:
        file.write(name + '\n')
        