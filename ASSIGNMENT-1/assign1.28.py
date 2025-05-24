# Sum of even numbers in a list
lst = [1, 2, 3, 4, 5, 6]
sum_even = 0
for num in lst:
    if num % 2 == 0:
        sum_even += num
print("Sum of even numbers:", sum_even)