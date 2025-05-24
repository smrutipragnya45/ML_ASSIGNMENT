# Merge Two Sorted Lists into One Sorted List
def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0
    # Merge the two lists
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    # Append remaining elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

# Example usage:
list1 = [1, 3, 5]
list2 = [2, 4, 6]
print("Merged list:", merge_sorted_lists(list1, list2))
