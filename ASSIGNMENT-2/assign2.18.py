# Find the Second Largest Number in a List
def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) >= 2 else None

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = second_largest(numbers)
print(f"Second largest number: {result}" if result is not None else "Not enough unique elements.")

