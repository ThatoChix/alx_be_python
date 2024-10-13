class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: adds two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: multiplies two numbers and references class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
