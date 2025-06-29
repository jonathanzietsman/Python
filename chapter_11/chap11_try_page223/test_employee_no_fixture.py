""" 
! test file with two test functions, test_give_default_raise() and test_give_custom_raise(). 
! Write tests without a fixture, and make sure they both pass.
"""

from employee import Employee

def test_give_default_raise():
    """Test that a default raise of $5000 is applied correctly."""
    emp = Employee('John', 'Doe', 50000)
    emp.give_raise()
    assert emp.annual_salary == 55000  # 50000 + 5000

def test_give_custom_raise():
    """Test that a custom raise is applied correctly."""
    emp = Employee('Jane', 'Smith', 60000)
    emp.give_raise(10000)
    assert emp.annual_salary == 70000  # 60000 + 10000
