class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Performs addition."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Performs multiplication and prints class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
