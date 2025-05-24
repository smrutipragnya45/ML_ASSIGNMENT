# Compute the Factorial of a Number Using Recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial: {factorial(num)}")
