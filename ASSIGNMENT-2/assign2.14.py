# Return a Dictionary of Character Frequencies in a String
def char_frequency(s):
    return {char: s.count(char) for char in set(s)}

text = input("Enter a string: ")
print(f"Character frequencies: {char_frequency(text)}")
