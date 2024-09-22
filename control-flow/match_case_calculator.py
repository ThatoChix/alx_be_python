# match_case_calculator.py

def calculator(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return num1 / num2
        case _:
            return "Invalid operation. Please choose from (+, -, *, /)."

def main():
    try:
        # Prompt user to input numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Ask for the operation
        operation = input("Choose the operation (+, -, *, /): ")
        
        # Perform the calculation and display the result
        result = calculator(num1, num2, operation)
        print(f"The result is: {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
