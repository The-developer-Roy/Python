# Python program to swap two variables without using a temporary variable

# Input variables
a = input("Enter the first value (a): ")
b = input("Enter the second value (b): ")

# Swap without temp
a, b = b, a

# Display the result
print(f"After swapping: a = {a}, b = {b}")
