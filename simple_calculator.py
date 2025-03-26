<<<<<<< HEAD
# Basic Calculator Program

def simple_calculator():
    try:
        # Ask the user to input the first number
        num1 = float(input("Enter the first number: "))
        
        # Ask the user to input the mathematical operation
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Ask the user to input the second number
        num2 = float(input("Enter the second number: "))

        # Perform the operation based on user input
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        else:
            result = "Invalid operation!"

        # Display the result with reference to input numbers
        if isinstance(result, (int, float)):
            print(f"{num1} {operation} {num2} = {result}")
        else:
            print(result)
    except ValueError:
        # Handle invalid numeric input
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    simple_calculator()

=======
# Basic Calculator Program

def simple_calculator():
    try:
        # Ask the user to input the first number
        num1 = float(input("Enter the first number: "))
        
        # Ask the user to input the mathematical operation
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Ask the user to input the second number
        num2 = float(input("Enter the second number: "))

        # Perform the operation based on user input
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        else:
            result = "Invalid operation!"

        # Display the result with reference to input numbers
        if isinstance(result, (int, float)):
            print(f"{num1} {operation} {num2} = {result}")
        else:
            print(result)
    except ValueError:
        # Handle invalid numeric input
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    simple_calculator()

>>>>>>> 6c479d650b6ce5f7294bf98fcc7dbeac24454033
