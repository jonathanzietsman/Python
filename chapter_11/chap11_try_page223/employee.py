class Employee:
    def __init__(self, first_name, last_name, salary):
        self.name = first_name
        self.age = last_name
        self.salary = salary
    
    def give_raise(self, amount=5000):
        self.salary += amount
        return self.salary
    
    
    
    
    
    
    
    
    
    
""" Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.
Write a test file for Employee with two test functions, test_give_default
_raise() and test_give_custom_raise(). Write your tests once without using a
fixture, and make sure they both pass. Then write a fixture so you don’t have to
create a new employee instance in each test function. Run the tests again, and
make sure both tests still pass. """