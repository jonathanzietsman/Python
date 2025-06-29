""" 
! class called Employee. __init__() method should take first name, last name, annual salary, store each of these as attributes. 
! method called give_raise() adds $5,000 to the annual salary by default but also accepts a different raise amount.
"""
class Employee:
    """
    A class to represent an employee.

    Attributes:
        first_name (str): The employee's first name.
        last_name (str): The employee's last name.
        annual_salary (float): The employee's yearly salary.
    """
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize first name, last name, and annual salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """
        Increase the annual salary by a default of $5000 or a custom amount.

        Parameters:
            amount (float): The raise amount. Defaults to 5000.
        """
        self.annual_salary += amount
