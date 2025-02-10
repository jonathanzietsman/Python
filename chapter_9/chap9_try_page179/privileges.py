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
