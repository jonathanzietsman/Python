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
        print(f'First Name: {self.first_name}, Last Name: {self.last_name}, Gender: {self.gender}, Date of Birth: {self.date_of_birth} ')
    # Make another method called greet_user() that prints a personalized greeting to the user.
    def greet_user(self):
        print(f'Welcome Back {self.first_name}!')
        
# Create several instances representing different users, and call both methods for each user.
user1 = User('Alice', 'Smith', 'Female', '1990-01-01')
user1.greet_user()
user1.describe_user()

user2 = User('Bob', 'Johnson', 'Male', '1985-05-15')
user2.greet_user()
user2.describe_user()

user3 = User('Charlie', 'Brown', 'Male', '2000-12-25')
user3.greet_user()
user3.describe_user()