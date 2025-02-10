from pathlib import Path

file = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page200\common_words.txt')

try:
    with open(file, 'r', encoding='utf-8') as f:
        # Convert to lowercase and split into words
        words = f.read().lower().split()  
        # Count occurrences of "the"
        the_count = words.count("the")  
        print(f"The word 'the' appears {the_count} times.")
except FileNotFoundError:
    print("Error: File not found!")
except UnicodeDecodeError:
    print("Error: Encoding issue. Ensure the file is saved as UTF-8.")
