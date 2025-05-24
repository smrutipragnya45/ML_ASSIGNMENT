#  Find the Least Common Multiple (LCM) of Two Numbers
def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a*b) // gcd(a, b)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"LCM: {lcm(x, y)}")
