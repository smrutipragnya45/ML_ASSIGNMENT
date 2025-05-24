# Check if a Number is an Armstrong Number
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return n == sum(d ** len(digits) for d in digits)

num = int(input("Enter a number: "))
print(f"{num} is {'an Armstrong' if is_armstrong(num) else 'not an Armstrong'} number.")
