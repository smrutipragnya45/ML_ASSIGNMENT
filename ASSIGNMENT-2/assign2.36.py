# Return a List of Tuples (Element, Index) from a List
def element_index_pairs(lst):
    return [(element, index) for index, element in enumerate(lst)]

# Example usage:
items = ['a', 'b', 'c']
print("Element-Index pairs:", element_index_pairs(items))