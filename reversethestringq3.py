test_string= (input("string: "))

def reverse(s):
    r = ""
    for i in s:
        r = i + r
    return r


print(reverse(test_string),"this is new string")