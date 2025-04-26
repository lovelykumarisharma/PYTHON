friends = ["Apple", "Orange" , 5 , 345.06, False, "Aakash" , "rohan"]

print(friends[0])
# list are not immutable
friends[0] = "grapes"

print(friends[0])

print(friends[1:5])

friends.append("srivar") #insertion in alist ...add kar diye at the end of the list
print(friends)

l1 = [1,4,3,7,5]
l1.sort() # help to ssort the list
print(l1)

l1.reverse()
print(l1) 


l1.insert(3, 456543)
print(l1)

l1.pop(3)
print(l1)