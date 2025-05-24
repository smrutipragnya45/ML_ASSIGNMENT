# Check if a List is Sorted
def is_sorted(lst):
    return lst == sorted(lst)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"The list is {'sorted' if is_sorted(numbers) else 'not sorted'}.")