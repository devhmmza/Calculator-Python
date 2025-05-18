# Calculator Program

# Function Definitions
def welcome():
    print("Welcome to the basic calculator")
    print("This calculator is capable of executing simple arithmetic operations")
    
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b

# Main Loop
while True:
    # Display welcome message
    welcome()

    try:
        # User Input Handling
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Please enter the operator (+, -, *, /): ")

        # Perform calculation
        if operator == '+':
            result = addition(num1, num2)
        elif operator == '-':
            result = subtraction(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid choice")
            continue 

        # Display Results
        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    # Ask if the user wants to perform another calculation
    again = input("Do you want to calculate again (yes/no): ").strip().lower()
    if again != 'yes':
        break


    
    
