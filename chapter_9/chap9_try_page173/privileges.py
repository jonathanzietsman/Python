""" Exercise 9-3 """
# Make a class called User
class User:
    # Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile.
    def __init__(self, first_name, last_name, gender, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth

    # Make a method called describe_user() that prints a summary of the user’s information
    def describe_user(self):
        print(f'First Name: {self.first_name}, Last Name: {self.last_name}, Gender: {self.gender}, Date of Birth: {self.date_of_birth}')

    # Make another method called greet_user() that prints a personalized greeting to the user.
    def greet_user(self):
        print(f'Welcome back, {self.first_name}!')

# Write a separate Privileges class
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = ["can add post", "can delete post", "can ban user"]
        else:
            self.privileges = privileges

    # Move the show_privileges() method to this class
    def show_privileges(self):
        print('Admin Privileges:')
        for privilege in self.privileges:
            print(f'- {privilege}')

# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3
class Admin(User):
    # Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on
    def __init__(self, first_name, last_name, gender, date_of_birth, privileges=None):
        super().__init__(first_name, last_name, gender, date_of_birth)
        # Make Privileges an attribute in the Admin class
        self.privileges = Privileges(privileges)

# Make a new instance of Admin and call the methods you wrote in the class
admin = Admin('John', 'Doe', 'Male', '1990-01-01')
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()
