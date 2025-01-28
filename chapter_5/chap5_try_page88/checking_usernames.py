# List of current users
current_users = ['John', 'Emily', 'Alex', 'Sophia', 'Michael']

# List of new users
new_users = ['john', 'Sophia', 'Chris', 'Daniel', 'Emma']

# Convert current_users to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Loop through new_users to check availability
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"Username '{new_user}' is available.")
