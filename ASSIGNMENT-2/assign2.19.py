# Return Only the Even Numbers from a List
def filter_even(lst):
    return [num for num in lst if num % 2 == 0]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Even numbers: {filter_even(numbers)}")
