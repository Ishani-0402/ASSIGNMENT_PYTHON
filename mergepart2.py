# Input two sorted lists
list1=[]
l1= int(input("length of list1: "))
for i in range(0, l1):
    ele = int(input())
    list1.append(ele)

list2=[]
l2= int(input("length of list2: "))
for i in range(0, l2):
    ele = int(input())
    list2.append(ele)

# Merge the lists
merged_list = sorted(list1 + list2)

# Display the merged list
print("Merged Sorted List:", merged_list)
