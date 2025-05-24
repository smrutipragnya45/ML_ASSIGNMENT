# Find the maximum in a list using loop
lst = [10, 50, 30, 40]
max_num = lst[0]
for num in lst:
    if num > max_num:
        max_num = num
print("Max:", max_num)