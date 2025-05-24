# Count frequency of digits in a number
num = input("Enter number: ")
freq = {}
for digit in num:
    freq[digit] = freq.get(digit, 0) + 1
print(freq)