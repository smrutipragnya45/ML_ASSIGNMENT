# Count How Many Times a Character Appears in a String
def count_char(s, ch):
    return s.count(ch)

text = input("Enter a string: ")
char = input("Enter a character to count: ")
print(f"Character '{char}' occurs {count_char(text, char)} times.")
