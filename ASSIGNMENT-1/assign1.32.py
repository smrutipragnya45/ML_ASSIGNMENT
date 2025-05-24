# Check if a number is a palindrome
num = input("Enter number: ")
print("Palindrome" if num == num[::-1] else "Not Palindrome")