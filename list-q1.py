movies=["yjhd","3 idiots","bahubali2","omg","omg2"]

#accessing the element in list
print("3rd movie from list :", movies[2])

#adding new movie to list
movies.append("jab we met")

#removing second movie from list
movies.pop(1)

#slicing the list
print("slicing to create new list:", movies[:3])
#looping through the list
print("list element:")
for movie in movies:
    print(movie)