# if elif else ladder...............
a= int(input("Enter your age: ")) # typecast bnana pada because we want to make it an integer

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