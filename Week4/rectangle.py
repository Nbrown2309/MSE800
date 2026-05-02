# rectangle.py

class RectangleLand:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate area
    def calculate_area(self):
        return self.length * self.width

    # Method to calculate perimeter
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    # Method to display results
    def display_info(self):
        print("\n--- Land Information ---")
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.calculate_area()}")
        print(f"Perimeter: {self.calculate_perimeter()}")