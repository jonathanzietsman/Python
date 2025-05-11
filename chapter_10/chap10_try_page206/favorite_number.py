# Import required modules
from pathlib import Path
import json

# Get the user's favorite number through console input
user_info = input('Favorite Number? ')

# Create a Path object pointing to our JSON file
path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page206\users_imformation.json')

# Convert the user's input to JSON format and write it to the file
# json.dumps() converts Python objects to a JSON string
contents = json.dumps(user_info)
# write_text() writes the JSON string to the file
path.write_text(contents)