# Print sum of digits of a number
num = int(input("Enter number: "))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print("Sum of digits:", sum_digits)