# while_loop.py

# Task: Calculate the sum of numbers until the user enters zero

total_sum = 0

# Keep prompting the user for input until they enter 0
while True:
    number = int(input("Enter a number (0 to quit): "))
    if number == 0:
        break  # Exit the loop if 0 is entered
    total_sum += number

# Output the total sum
print(f"The total sum is: {total_sum}")
