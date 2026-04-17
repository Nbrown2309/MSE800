# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    # Check to avoid division by zero
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Function for modulus (remainder)
def modulus(a, b):
    return a % b

# Function to calculate factorial
def factorial(n):
    # Factorial only works with positive integers
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Main program
def main():
    print("Basic Calculator")
    print("Operations: +, -, *, /, %, ! (factorial)")

    operator = input("Enter operator: ")

    # Factorial only needs one number
    if operator == "!":
        num = int(input("Enter a number: "))
        print("Result:", factorial(num))

    else:
        # Accept numbers (can also accept complex numbers like 2+3j)
        num1 = complex(input("Enter first number: "))
        num2 = complex(input("Enter second number: "))

        if operator == "+":
            print("Result:", add(num1, num2))

        elif operator == "-":
            print("Result:", subtract(num1, num2))

        elif operator == "*":
            print("Result:", multiply(num1, num2))

        elif operator == "/":
            print("Result:", divide(num1, num2))

        elif operator == "%":
            # Modulus does NOT work with complex numbers
            if isinstance(num1, complex) or isinstance(num2, complex):
                print("Error: Modulus does not support complex numbers")
            else:
                print("Result:", modulus(num1, num2))

        else:
            print("Invalid operator")

# Run the program
main()