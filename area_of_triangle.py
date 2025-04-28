# Python program to calculate the area of a triangle using Heron's formula

import math

# Input the sides of the triangle
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Display the result
print(f"The area of the triangle is {area}")




# # Python program to calculate the area of a triangle

# # Input the base and height
# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))

# # Calculate the area
# area = (base * height) / 2

# # Display the result
# print(f"The area of the triangle is {area}")
