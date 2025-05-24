# Return a Dictionary of Word Counts from a String
def word_count(s):
    words = s.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

# Example usage:
text = "hello world hello"
print("Word counts:", word_count(text))