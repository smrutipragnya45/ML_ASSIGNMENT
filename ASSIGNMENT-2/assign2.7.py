# Calculate the Sum of a List of Numbers
def sum_list(lst):
    return sum(lst)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Sum: {sum_list(numbers)}")