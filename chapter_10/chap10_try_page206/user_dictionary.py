from pathlib import Path
import json

# Define a constant for the file path where the user's information will be stored
# Using a constant makes it easier to change the file location if needed
FILE_PATH = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page206\user.txt')

def get_stored_user_info(file_path):
    """
    Retrieve and return the stored user information from the file.

    Steps:
    1. Check if the file exists.
    2. Read the file content and remove any extra whitespace.
    3. If content exists, attempt to decode it from JSON.
    4. Verify the decoded data is a dictionary containing the keys 'name', 'age', and 'color'.
    5. Return the dictionary if valid; otherwise, return None.

    Args:
        file_path: Path object pointing to the file containing user information

    Returns:
        dict: Dictionary containing user information if valid, None otherwise
    """
    if file_path.exists():
        # Read the file's content and remove leading/trailing whitespace
        contents = file_path.read_text().strip()
        if contents:  # Only proceed if the file is not empty
            try:
                # Decode the JSON string back into a Python object (expected to be a dictionary)
                user_info = json.loads(contents)
                # Check that the expected keys exist in the dictionary
                if all(key in user_info for key in ("name", "age", "color")):
                    return user_info
                else:
                    return None
            except json.JSONDecodeError:
                # If the file content is not valid JSON, return None
                return None
    # If the file does not exist or is empty, return None
    return None

def get_new_user_info(file_path):
    """
    Prompt the user for their information (name, age, and favorite color),
    ensuring valid (non-empty) inputs and that age is a valid integer.

    Steps:
    1. Continuously prompt for name until a non-empty string is received
    2. Continuously prompt for age until a valid integer is provided
    3. Continuously prompt for favorite color until a non-empty string is received
    4. Store the collected information in a dictionary
    5. Write the dictionary to the file in JSON format
    6. Return the newly collected user information

    Args:
        file_path: Path object pointing to where the user information should be saved

    Returns:
        dict: Dictionary containing the newly collected user information
    """
    # Prompt the user for their name
    while True:
        name = input("What's your name? ").strip()
        if name:  # Accept the input if it is not empty
            break
        print("Please enter a valid name, not an empty value.")
    
    # Prompt the user for their age and ensure it's a valid integer
    while True:
        age_input = input("What's your age? ").strip()
        if age_input:
            try:
                age = int(age_input)
                break  # Exit the loop if a valid integer is provided
            except ValueError:
                print("Please enter a valid integer for your age.")
        else:
            print("Age cannot be empty. Please enter your age.")
    
    # Prompt the user for their favorite color
    while True:
        color = input("What's your favorite color? ").strip()
        if color:  # Accept the input if it is not empty
            break
        print("Please enter a valid favorite color, not an empty value.")
    
    # Create a dictionary containing all of the user's information
    user_info = {"name": name, "age": age, "color": color}
    # Write the dictionary to the file in JSON format
    file_path.write_text(json.dumps(user_info))
    return user_info  # Return the newly collected user information

def greet_user():
    """
    Greet the user using stored information if available, or prompt for new information.

    Steps:
    1. Attempt to retrieve the stored user information from the file
    2. If valid information is found, print a personalized welcome message with all details
    3. If no valid information is found, prompt the user for their details, store them, and greet them
    """
    # Attempt to retrieve stored user information
    user_info = get_stored_user_info(FILE_PATH)
    
    if user_info:
        # If valid information was found, greet the user and display their details
        print(f"Welcome back, {user_info['name']}!")
        print(f"I remember that you are {user_info['age']} years old and your favorite color is {user_info['color']}.")
    else:
        # If no stored information is found, prompt the user for new details
        user_info = get_new_user_info(FILE_PATH)
        print(f"We'll remember you when you come back, {user_info['name']}!")
        print(f"You are {user_info['age']} years old and your favorite color is {user_info['color']}.")

# Start the program by greeting the user
greet_user()
