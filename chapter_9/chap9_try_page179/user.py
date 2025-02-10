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
        
        