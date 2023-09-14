original_list=[]
l= int(input("length of list: "))
# iterating till the range
for i in range(0, l):
    ele = int(input())
    original_list.append(ele)

largest = original_list[0]
for num in original_list:
  if num > largest:
    largest = num

print(largest)