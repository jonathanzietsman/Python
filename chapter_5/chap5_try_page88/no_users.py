# hello_admin.py
# List of 5 usernames including 'admin'
usernames = ['admin', 'user1', 'user2', 'user3', 'user4']
""" usernames = [] """
# if test that list not empty
if not usernames:
    print("We need to find some users!")

else:
    # If username is admin print special gretting 
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")

