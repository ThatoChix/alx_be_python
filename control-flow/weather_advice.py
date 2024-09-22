# control_flow.py

# Task: Determine whether a number is positive, negative, or zero

# Ask for user input
number = int(input("Enter a number: "))

# Control flow using if-else
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print(f"{number} is zero.")
