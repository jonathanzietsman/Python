from pathlib import Path
import json

# Define file path
path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page206\users_imformation.json')

try:
    # Read the file and remove leading/trailing spaces
    load_contents = path.read_text().strip()
    
    if load_contents:
        # Convert JSON string back to Python data
        user_fav_nmbr = json.loads(load_contents)
        # Check if the loaded favorite number is not empty and is an integer.
        if not user_fav_nmbr or not isinstance(user_fav_nmbr, int):
            raise FileNotFoundError
        print(f"I know your favorite number! It’s {user_fav_nmbr}")
    else:
        raise FileNotFoundError
except (FileNotFoundError, json.JSONDecodeError):
    # Keep prompting until a valid integer is entered
    while True:
        user_input = input("You haven't told me your favorite number yet. What is it? ")
        # Check if input is empty
        if not user_input.strip():
            print("You must enter a valid integer, not an empty value.")
            continue
        try:
            user_fav_nmbr = int(user_input)
            break  # Valid integer entered, exit the loop.
        except ValueError:
            print("That's not a valid integer. Please try again.")
    
    # Save the valid integer in JSON format
    path.write_text(json.dumps(user_fav_nmbr))
    print(f"Got it! I'll remember that your favorite number is {user_fav_nmbr}.")
