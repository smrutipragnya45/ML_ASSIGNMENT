# Find the Most Frequent Element in a List
def most_frequent(lst):
    return max(set(lst), key=lst.count)

# Example usage:
numbers = [1, 2, 2, 3, 3, 3, 4]
print("Most frequent element:", most_frequent(numbers))