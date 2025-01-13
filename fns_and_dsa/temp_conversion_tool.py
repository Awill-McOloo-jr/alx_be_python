# temp_conversion_tool.py

# Define the global conversion factors exactly as expected by the checker
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # Conversion factor for Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # Conversion factor for Celsius to Fahrenheit

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main function to interact with the user
def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))  # Input temperature
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()  # Celsius or Fahrenheit

        if unit == 'C':
            # Convert Celsius to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        elif unit == 'F':
            # Convert Fahrenheit to Celsius
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
