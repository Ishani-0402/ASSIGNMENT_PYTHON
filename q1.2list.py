def common_elements(list1, list2):
    common = []
    for e in list1:
        if e in list2:
            common.append(e)
    return common

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


common = common_elements(list1, list2)
print(common)