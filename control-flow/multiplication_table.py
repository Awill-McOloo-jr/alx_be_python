# Prompt the user to enter a number for the multiplication table
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table using a for loop
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
