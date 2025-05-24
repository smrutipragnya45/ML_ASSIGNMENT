# Write a function to check if a number is prime
def is_prime(n,i=2):
    if(n<=2):
        return True if n==2 else False
    if(n%i==0):
        return False
    if(i*i>n):
        return True
    return is_prime(n,i+1)
number=int(input("enter the number:"))
if is_prime(number):
    print("prime number")
else:
    print("not a prime number")