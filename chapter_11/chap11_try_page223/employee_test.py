from employee import Employee
import pytest

@pytest.fixture
def example():
    """Create and return a sample Employee instance for testing."""
    return Employee('Jack', 'Smith', 50000)

def test_give_default_raise(example):
    """Test that the default raise amount of $5000 is correctly applied."""
    result = example.give_raise()
    assert result == 55000

def test_give_custom_raise(example):
    """Test that a custom raise amount is correctly applied."""
    result = example.give_raise(10000)
    assert result == 60000
