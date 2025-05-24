# Return the Index of a Value in a List (or -1)
def find_index(lst, value):
    try:
        return lst.index(value)
    except ValueError:
        return -1

# Example usage:
items = [10, 20, 30, 40]
print("Index of 30:", find_index(items, 30))
print("Index of 50:", find_index(items, 50))