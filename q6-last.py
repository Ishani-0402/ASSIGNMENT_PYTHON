def merge_sorted_lists(list1, list2):
    merged_list = []
    i = 0  # Pointer for list1
    j = 0  # Pointer for list2

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append any remaining elements from list1 and list2
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

# Input two lists from the user
list1 = []
l1 = int(input("Length of list1: "))
for i in range(l1):
    ele = int(input())
    list1.append(ele)

list2 = []
l2 = int(input("Length of list2: "))
for i in range(l2):
    ele = int(input())
    list2.append(ele)

# Sort the input lists
list1.sort()
list2.sort()

# Merge the sorted lists
merged_list = merge_sorted_lists(list1, list2)

# Display the merged sorted list
print("Merged Sorted List:", merged_list)
