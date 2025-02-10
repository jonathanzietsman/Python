from employee import Employee
import pytest

@pytest.fixture

def example():
    return Employee('Jack', 'Smith', 50000)

def test_give_default_raise(example):
    result = example.give_raise()
    assert result == 55000

def test_give_custom_raise(example):
    result = example.give_raise(10000)
    assert result == 60000
    
    
    
    
    
    
    
    
    
    
    
    
    
    
""" 
from employee import Employee
import pytest    
    
def test_give_default_raise():
    test_default = Employee('Jack', 'Smith', 50000)
    result = test_default.give_raise()
    assert result == 55000

def test_give_custom_raise():
    test_custom = Employee('Jack', 'Smith', 50000)
    result = test_custom.give_raise(10000)
    assert result == 60000
"""    
    
