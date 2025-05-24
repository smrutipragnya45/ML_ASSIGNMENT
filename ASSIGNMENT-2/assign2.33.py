# Return the Median of a List
def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

# Example usage:
numbers = [5, 2, 9, 1, 5, 6]
print("Median:", median(numbers))