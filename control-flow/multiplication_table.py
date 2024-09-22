# multiplication_table.py

def print_multiplication_table(number):
    # Loop through numbers 1 to 10 and print the multiplication table
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

def main():
    try:
        # Prompt user to input a number
        number = int(input("Enter a number to see its multiplication table: "))
        
        # Call the function to print the multiplication table
        print_multiplication_table(number)
    
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()
