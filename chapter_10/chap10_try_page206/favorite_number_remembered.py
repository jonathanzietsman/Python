# Import required modules
from pathlib import Path
import json

# Create a Path object pointing to our JSON file
path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page206\users_imformation.json')

try:
    # Attempt to read the existing favorite number from the file
    # strip() removes any leading/trailing whitespace
    load_contents = path.read_text().strip()
    
    if load_contents:
        # Convert the JSON string back to a Python object
        user_fav_nmbr = json.loads(load_contents)
        # Validate that the loaded number is not empty and is an integer
        if not user_fav_nmbr or not isinstance(user_fav_nmbr, int):
            raise FileNotFoundError
        print(f"I know your favorite number! It's {user_fav_nmbr}")
    else:
        raise FileNotFoundError
except (FileNotFoundError, json.JSONDecodeError):
    # If no valid favorite number exists, prompt the user for input
    while True:
        user_input = input("You haven't told me your favorite number yet. What is it? ")
        # Ensure the input is not empty
        if not user_input.strip():
            print("You must enter a valid integer, not an empty value.")
            continue
        try:
            # Convert the input to an integer
            user_fav_nmbr = int(user_input)
            break  # Exit the loop if a valid integer was entered
        except ValueError:
            print("That's not a valid integer. Please try again.")
    
    # Save the new favorite number to the file in JSON format
    path.write_text(json.dumps(user_fav_nmbr))
    print(f"Got it! I'll remember that your favorite number is {user_fav_nmbr}.")
