# robust_division_calculator.py
def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division, check for division by zero
        if denominator == 0:
            return "Error: Cannot divide by zero."
        else:
            result = numerator / denominator
            return f"The result of the division is {result}"
    
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
    except Exception as e:
        # Catch any other unforeseen errors
        return f"An unexpected error occurred: {str(e)}"
