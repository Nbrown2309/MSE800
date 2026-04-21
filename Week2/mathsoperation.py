# Creating a Object Orientated programming PD

# Developing the classes for the calculator 
class Calculator:
    def __init__(self, num1, num2):
        # Initializer (constructor)
        self.num1 = num1
        self.num2 = num2

    # Method 1 - Addition
    def add(self):
        return self.num1 + self.num2

    # Method 2 - subtract
    def subtract(self):
        return self.num1 - self.num2

    # method 3 multiply
    def multiply(self):
        return self.num1 * self.num2
    
    # method 4 - division
    def divide(self):
        if self.num2 == 0:
            return "Error: Cannot divide by zero"
        return self.num1 / self.num2

    # Method 5 - display result
    def display_result(self, operation, result):
        print(f"Result of {operation}: {result}")


# function 1 - Get the users input
def get_numbers():
    num1 = float(input("Enter in first number: "))
    num2 = float(input("Enter in second number: "))
    return num1, num2

# function 2 - Run the calculator / creating a menu system aswell
def run_calculator():
    while True:
        print("\n=== Calculator Menu ===")
        print("1. Addition ")
        print("2. Subtraction")
        print("3. Multiplication")
        print ("4. Division ")
        print ("5. Exit Manu")

        choice = input("Choose an option...")

        if choice == "5":
            print("Exiting Caculator...")
            break
        
        elif choice in ["1", "2", "3", "4", "5"]:
            num1, num2 =get_numbers()
            calc = Calculator(num1, num2)

            if choice == "1":
                result = calc.add()
                calc.display_result("Addition", result)

            elif choice == "2":
                result = calc.subtract()
                calc.display_result("subtraction", result)

            elif choice == "3":
                result = calc.multiply()
                calc.display_result("Multiplication", result)

            elif choice == "4":
                result = calc.divide()
                calc.display_result("Division", result)
        
        else:
            print("Invalid Choice Please Try Again!!")


# Run the following Program
run_calculator()