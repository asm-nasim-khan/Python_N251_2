# calculator.py

class Calculator:
    """A simple calculator class to demonstrate doctest usage."""

    def add(self, a, b):
        """
        Returns the sum of a and b.

        >>> calc = Calculator()
        >>> calc.add(2, 3)
        5
        >>> calc.add(-1, 1)
        0
        """
        return a + b

    def subtract(self, a, b):
        """
        Returns the difference when b is subtracted from a.

        >>> calc = Calculator()
        >>> calc.subtract(10, 5)
        5
        >>> calc.subtract(0, 1)
        -1
        """
        return a - b

    def multiply(self, a, b):
        """
        Returns the product of a and b.

        >>> calc = Calculator()
        >>> calc.multiply(3, 5)
        15
        >>> calc.multiply(-1, 1)
        -1
        """
        return a * b

    def divide(self, a, b):
        """
        Returns the quotient of a divided by b.

        >>> calc = Calculator()
        >>> calc.divide(10, 2)
        5.0
        >>> calc.divide(3, 2)
        1.5
        >>> calc.divide(10, 0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot divide by zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

if __name__ == "__main__":
    import doctest
    doctest.testmod()