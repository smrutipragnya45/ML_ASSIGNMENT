# Check if a Sentence is a Pangram
import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))

# Example usage:
sentence = "The quick brown fox jumps over the lazy dog"
print("Is pangram:", is_pangram(sentence))