# Compute the Power of a Number Using Recursion
def power(base, exponent):
    return 1 if exponent == 0 else base * power(base, exponent - 1)

b = float(input("Enter base: "))
e = int(input("Enter exponent: "))
print(f"{b} raised to the power {e} is {power(b, e)}")
