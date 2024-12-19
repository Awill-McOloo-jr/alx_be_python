# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the rows
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print the asterisks for each row
    for col in range(size):
        print("*", end="")  # Print asterisk without moving to the next line
    print()  # Print a newline after each row
    
    row += 1  # Increment the row counter
