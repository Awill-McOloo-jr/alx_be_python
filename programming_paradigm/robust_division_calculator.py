# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division with error handling for division by zero and non-numeric input."""
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division and return the result
        result = numerator / denominator
        return f"Result: {result:.2f}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Non-numeric input. Please provide valid numbers."
