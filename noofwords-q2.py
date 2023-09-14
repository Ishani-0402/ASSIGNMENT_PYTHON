# Python3 code to demonstrate
# to count words in string
# using split()

# initializing string
test_string= (input("string: "))



# printing original string
print("The original string is : " + test_string)

# using split()
# to count words in string
res = test_string.count(" ")+1

# printing result
print("The number of words in string are : " + str(res))
print("The number of letters in string are : ", len(test_string))
