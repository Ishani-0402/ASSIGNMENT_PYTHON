original_list=[]
l= int(input("length of list: "))
# iterating till the range
for i in range(0, l):
    ele = int(input())
    original_list.append(ele)

new_list = [original_list[len(original_list) - i]
			for i in range(1, len(original_list)+1)]
print(new_list)
