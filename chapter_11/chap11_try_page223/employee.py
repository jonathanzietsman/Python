class Employee:
    """A class to represent an employee with basic information and salary management."""
    
    def __init__(self, first_name, last_name, salary):
        """Initialize an Employee instance."""
        self.first_name = first_name  
        self.last_name = last_name    
        self.salary = salary
    
    def give_raise(self, amount=5000):
        """Increase the employee's salary by the specified amount."""
        self.salary += amount
        return self.salary
