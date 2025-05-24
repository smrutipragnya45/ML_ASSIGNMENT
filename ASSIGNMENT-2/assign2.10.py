# Find the Minimum Value in a List
def min_in_list(lst):
    return min(lst)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Minimum value: {min_in_list(numbers)}")