# GCD of two numbers using loop
a, b = 60, 48
gcd = 1
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i
print("GCD:", gcd)