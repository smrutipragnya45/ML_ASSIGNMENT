# Find the Sum of Digits of a Number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

num = int(input("Enter a number: "))
print(f"Sum of digits: {sum_of_digits(num)}")
