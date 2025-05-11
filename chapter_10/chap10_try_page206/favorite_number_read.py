# This program reads a user's favorite number from a JSON file
# It demonstrates how to use JSON for data retrieval and deserialization

# Import required modules
from pathlib import Path
import json

# Create a Path object pointing to our JSON file
path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page206\users_imformation.json')

# Read the JSON string from the file
contents = path.read_text()

# Convert the JSON string back to a Python object
# json.loads() parses the JSON string into a Python object
user_fav_nmbr = json.loads(contents)

# Display the user's favorite number in a friendly message
print(f"I know your favorite number! It's {user_fav_nmbr}")