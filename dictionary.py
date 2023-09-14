#creating a dictionary of stu inf
lib={
    "jungle book":"ishani",
    "life book":"montu",
    "makeup book":"rito",
    "talent book":"debo"
}
#adding a new key value pair to dictionary
lib["pagal book"]="nifty"

#looping through the items
print("list element:")
for key ,value in lib.items():
    print(key,";", value)