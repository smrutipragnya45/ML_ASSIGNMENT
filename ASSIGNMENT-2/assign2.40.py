# Count Uppercase and Lowercase Characters in a String
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# Example usage:
text = "Hello World!"
upper_count, lower_count = count_case(text)
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)