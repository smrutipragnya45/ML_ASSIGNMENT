# Return the Average of a List of Numbers
def average(lst):
    return sum(lst) / len(lst) if lst else 0

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Average: {average(numbers)}")
