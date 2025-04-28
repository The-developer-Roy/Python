num = int(input("Enter any number: "))

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fact(n-1)

print(f"the factorial of {num} is {fact(num)}")