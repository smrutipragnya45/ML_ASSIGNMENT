# Prime number check using loop
num = int(input("Enter number: "))
is_prime = True
if num < 2:
    is_prime = False
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not Prime")