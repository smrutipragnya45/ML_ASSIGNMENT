# Count uppercase and lowercase letters in a string
s = "Hello World"
upper = lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase:", upper, "Lowercase:", lower)