s= {} #empty dict
marks = {
    "harry" : 100,
    "shubham": 56,
    "rohan" : 23,
    1: "harryaa"
  
}
print(marks, type(marks))

print(marks["harry"])

# marks = [["harry",100], ["rohan",64],]
# methods


print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"harry":99, "ranuka": 00})
print(marks)

print(marks.get("harry2")) #prints none
# difference
print(marks["harry2"]) #returns erroe