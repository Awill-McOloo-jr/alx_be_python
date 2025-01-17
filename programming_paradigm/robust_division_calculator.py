# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division with error handling for division by zero and non-numeric input."""
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division and return the result
        result = numerator / denominator
        return f"The result of the division is {result:.1f}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
