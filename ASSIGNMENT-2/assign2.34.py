# Find the Intersection of Two Lists
def intersection(list1, list2):
    return list(set(list1) & set(list2))

# Example usage:
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print("Intersection:", intersection(list1, list2))