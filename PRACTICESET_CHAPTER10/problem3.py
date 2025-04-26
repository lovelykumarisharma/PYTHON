class demo:
    a = 4

o = demo()
print(o.a) #prints the class atrib ute because the instance attribute is not presant

o.a = 0 #instance attribute is set
print(o.a) #prints the instance attribute because instance attribute is presant

print(demo.a) #print the class attribute