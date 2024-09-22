# control_and_loop.py

# Task: Ask for user input in a loop and determine if the number is odd or even

while True:
    # Ask for a number
    number = int(input("Enter a number (0 to quit): "))
    
    # Check for termination condition
    if number == 0:
        print("Exiting program.")
        break
    
    # Use control flow to determine if the number is odd or even
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
