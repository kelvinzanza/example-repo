# User input on first and second number
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Print out for user to read
print("What would you like to do: ")

# Ask user input on the operator
operator = input("+ or -")

# If statment to check condition and print asnwer
if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
else:
    print("Sorry that was not asked")