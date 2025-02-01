class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        :param a: First number.
        :param b: Second number.
        :return: Sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers and print the calculation type.
        
        :param a: First number.
        :param b: Second number.
        :return: Product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b