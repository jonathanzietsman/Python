""" 
! write a fixture. Run the tests again, and make sure both tests still pass
"""
import pytest
from employee import Employee

# ---- Fixture ----
@pytest.fixture
def employee():
    """
    Provide a fresh Employee instance before each test.
    Pytest will inject this fixture into any test that accepts 'employee' as a parameter.
    """
    return Employee('Alice', 'Johnson', 75000)

# ---- Tests ----
def test_give_default_raise(employee):
    """Test that a default raise of $5000 is applied correctly using fixture."""
    employee.give_raise()
    assert employee.annual_salary == 80000  # 75000 + 5000

def test_give_custom_raise(employee):
    """Test that a custom raise is applied correctly using fixture."""
    employee.give_raise(15000)
    assert employee.annual_salary == 90000  # 75000 + 15000
