# Write a function to check if a string is a palindrome
def reverse(s):
    reversed_str=""
    for char in s:
        reversed_str=char+reversed_str
    if(reversed_str==s):
        return True
    else:
        return False
s=input("enter the text:")
print("is pallindrome?",reverse(s))