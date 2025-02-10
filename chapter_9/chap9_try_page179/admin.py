from user import User
from privileges import Privileges

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