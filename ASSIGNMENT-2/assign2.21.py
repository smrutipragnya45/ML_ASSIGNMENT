# Calculate the Greatest Common Divisor (GCD) of Two Numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"GCD: {gcd(x, y)}")
