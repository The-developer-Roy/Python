# Taking a number from user as an input
num = int(input("Enter a number: "))

# Adding conditions to check whether the given number is positive, negative or zero

if num>0:
    print(f"{num} is positive")
elif num<0:
    print(f"{num} is negative")
else:
    print(f"{num} is equal to zero")