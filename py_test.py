import pytest
from calc import Calculator


calc = Calculator()

def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(-1, -1) == -2

def test_subtract():
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(-1, 1) == -2
    assert calc.subtract(-1, -1) == 0

def test_multiply():
    assert calc.multiply(3, 5) == 15
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(-1, -1) == 1

def test_divide():
    assert calc.divide(10, 2) == 5
    assert calc.divide(-1, 1) == -1
    assert calc.divide(-1, -1) == 1

    # Testing division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.divide(10, 0)