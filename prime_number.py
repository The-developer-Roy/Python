import math

# Input a number
num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num > 1:
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
