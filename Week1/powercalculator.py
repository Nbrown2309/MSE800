# Power Calculator

def calculate_power(x, y):
    return x ** y

# User input
try:
    x = float(input("Enter Base (x): "))
    y = float(input("Enter Base (y): "))

    result = calculate_power(x, y)

    print(f"{x} ^ {y} = {result}")

except ValueError:
    print("Invalid input. PLease enter numbers only.")