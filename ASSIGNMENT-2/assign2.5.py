# Create a function to count the number of vowels in a string
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in 'aeiou')
print("vowel count is:",count_vowels("areo"))
    # count=s
    # for ch in s:
    #     if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' ch=='E' or ch=='I' or ch=='O' or ch=='U'):


