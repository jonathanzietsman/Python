# Import the Path class from pathlib for handling file paths
from pathlib import Path

# Create a Path object pointing to our text file
file = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page200\common_words.txt')

# Use a try-except block to handle potential file reading errors
try:
    # Open the file in read mode with UTF-8 encoding
    # The 'with' statement ensures the file is properly closed after reading
    with open(file, 'r', encoding='utf-8') as f:
        # Read the entire file, convert to lowercase, and split into words
        # This makes the word count case-insensitive
        words = f.read().lower().split()  
        
        # Count how many times "the" appears in the text
        the_count = words.count("the")  
        print(f"The word 'the' appears {the_count} times.")
except FileNotFoundError:
    # Handle the case where the file doesn't exist
    print("Error: File not found!")
except UnicodeDecodeError:
    # Handle the case where the file encoding is incorrect
    print("Error: Encoding issue. Ensure the file is saved as UTF-8.")
