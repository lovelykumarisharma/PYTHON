name = input("enter your name: ")
# print(name.capitalize())
print(f"good afternoon,{name.capitalize()}")


# problem 2

lettor = ''' Dear <|name|>,
          you are selected!
          <|date|> '''

print(lettor.replace(" <|name|>", "srivar").replace("  <|date|","04 MARCH 2025"))

# problem 3
# to detect double space in any string
name = "hary is a  good boy and a bad boy also"
# fing function returns substring occurance in the parent string
print(name.find("  "))
print(name.find("bad"))


# problem 4
# replace karna h

print(name.replace("  ",""))   #strings are immumtable by mean you cannot change then by runing sunction or by 


# problem 5
lettor = "Dear Harry \n  \t This PYTHON Cource Is NICE \n\tTHANKS"
print(lettor)