# Reverse a List
def reverse_list(lst):
    return lst[::-1]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Reversed list: {reverse_list(numbers)}")
