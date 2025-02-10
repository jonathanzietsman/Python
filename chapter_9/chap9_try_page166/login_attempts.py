# Make a class called User
class User:
    # Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile.
    #! Add login_attempts attribute 
    def __init__(self, first_name, last_name, gender, date_of_birth, login=0):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.login = login
    # Make a method called describe_user() that prints a summary of the user’s information
    def describe_user(self):
        print(f'First Name: {self.first_name}, Last Name: {self.last_name}, Gender: {self.gender}, Date of Birth: {self.date_of_birth} ')
    # Make another method called greet_user() that prints a personalized greeting to the user.
    def greet_user(self):
        print(f'Welcome Back {self.first_name}!')
    
    
    def login(self):
        self.login = 0
    
    
    #! method called increment_login_attempts() that increments the value of login_attempts by 1
    def increment_login_attempts(self):
        self.login += 1
        
    #! method called reset_login_attempts() that resets the value of login_attempts to 0.
    def reset_login_attempts(self):
        self.login = 0
        

# Create several instances representing different users, and call both methods for each user.
user1 = User('Alice', 'Smith', 'Female', '1990-01-01')
user1.greet_user()
user1.describe_user()

user2 = User('Bob', 'Johnson', 'Male', '1985-05-15')
user2.greet_user()
user2.describe_user()

#! Make an instance of the User class and call increment_login_attempts() several times
user3 = User('Charlie', 'Brown', 'Male', '2000-12-25')
user3.increment_login_attempts()
user3.increment_login_attempts()
#! Print the value of login_attempts to make sure it was incremented properly
print(f'Login Attempts: {user3.login}')
#! call reset_login_attempts()
user3.reset_login_attempts()
#! Print login_attempts again to make sure it was reset to 0.
print(f'Login Attempts: {user3.login}')