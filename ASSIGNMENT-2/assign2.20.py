# Check if All Characters in a String are Unique
def all_unique(s):
    return len(set(s)) == len(s)

text = input("Enter a string: ")
print(f"All characters are {'unique' if all_unique(text) else 'not unique'}.")
