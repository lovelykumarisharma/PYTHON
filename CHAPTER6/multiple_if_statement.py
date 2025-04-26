
a= int(input("Enter your age: ")) 

# if atatement 1
if(a%2 == 0):
    print("a is even: ")

# End of if statement no. 1..........


# if ataement no. 2
if(a>=18):
    # indentation space khte h isko
    print("you are above the age of consent")
    print("good for you...")

elif(a<0):
    print("you'r entring an invalid age")

elif(a==0):
    print("you are entring 0 which is not a valid age")


else:
    print("you are below the age of consent")

print("end of program!")
# End of if satement no. 2...