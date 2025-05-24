# Write a function to reverse a string
def reverse(s):
    reversed_str=""
    for char in s:
        reversed_str=char+reversed_str
    return reversed_str
text=input("enter string:")
print("reversed text is:",reverse(text))