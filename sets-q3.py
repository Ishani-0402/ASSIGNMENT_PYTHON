language={"c","c++","javascript"}

#addin elemnt to the sets
language.add("python")

#removing elements to tje sets
language.remove("c")

#checking if element is present in sets
print("print if python is in language:", "python"in language)

language2={"css","html ","java","python"}

intersection_result = language & language2

print(intersection_result)

