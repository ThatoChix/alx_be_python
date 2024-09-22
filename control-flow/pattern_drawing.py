def draw_pattern(size):
    # While loop to iterate through each row
    row = 0
    while row < size:
        # For loop to print asterisks side by side in each row
        for col in range(size):
            print("*", end="")
        # Move to the next line after completing each row
        print()
        row += 1

# Example: drawing a pattern of size 4
draw_pattern(4)
