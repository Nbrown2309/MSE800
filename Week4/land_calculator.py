# main.py

from rectangle import RectangleLand

print("=== Rectangular Land Calculator ===")

# User input
length = float(input("Enter the length of the land: "))
width = float(input("Enter the width of the land: "))

# Create object
land = RectangleLand(length, width)

# Display calculations
land.display_info()