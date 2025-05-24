# Return All Prime Numbers up to n
def primes_up_to(n):
    primes = []
    for num in range(2, n+1):
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            primes.append(num)
    return primes

n = int(input("Enter a number: "))
print(f"Prime numbers up to {n}: {primes_up_to(n)}")
