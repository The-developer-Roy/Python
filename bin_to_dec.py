import math

# Function to count the number of digits in a number
def digitcounter(bin_num):
    if bin_num == 0:
        return 1
    count = 0
    while bin_num != 0:
        bin_num //= 10
        count += 1
    return count

# Function to reverse a number
def reverseNumber(num):
    reversed_num = 0
    while num != 0:
        remainder = num % 10
        reversed_num = reversed_num * 10 + remainder
        num //= 10
    print(reversed_num)
    return reversed_num

# Function to extract digits and store them in an array
def extractDigits(num, size):
    digits = []
    num = abs(num)  # Ensure positive number
    for _ in range(size):
        digits.append(num % 10)
        num //= 10
    return digits

# Main function
def main():
    bin_num = int(input("Enter your binary number: "))

    # Get the number of digits
    m = digitcounter(bin_num)

    # Extract digits in reverse order
    digits = extractDigits(bin_num, m)

    # Convert binary to decimal
    decimal_sum = sum(digits[i] * math.pow(2, i) for i in range(m))

    print(f"The decimal equivalent of binary number {bin_num} is = {int(decimal_sum)}")

if __name__ == "__main__":
    main()
