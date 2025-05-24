# Check if a Number is a Perfect Number
def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

num = int(input("Enter a number: "))
print(f"{num} is {'a perfect' if is_perfect(num) else 'not a perfect'} number.")
