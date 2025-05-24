# Return the Longest Word in a Sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ''

text = input("Enter a sentence: ")
print(f"Longest word: {longest_word(text)}")
