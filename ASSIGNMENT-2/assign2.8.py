# Return the Fibonacci Sequence up to n Terms
def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

n = int(input("Enter number of terms: "))
print(f"Fibonacci sequence: {fibonacci(n)}")

