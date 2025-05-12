from main_pytest import Product
from dataclasses import is_dataclass
import pytest

@pytest.fixture
def product():
    """Fixture to create a product."""
    return Product(1, 'test', 1.0, 10)

def test_constructor(product):
    """Test the constructor of the class."""
    assert product.id == 1
    assert product.name == 'test'
    assert product.price == 1.0
    assert product.stock == 10

def check_if_it_is_a_dataclass(product):
    """Check if the class is a dataclass."""
    assert is_dataclass(product) == True

def test_increase_stock(product):
    """Test the increase_stock method."""
    product.increase_stock(10)
    assert product.stock == 20

def test_decrease_stock(product):
    """Test the decrease_stock method."""
    product.decrease_stock(8)
    assert product.stock == 2