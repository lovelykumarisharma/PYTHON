f= open("chapter9/myfile.txt")
print(f.read())
f.close()



# the same can be written using with statement like this:
with open("file.txt") as f:
    proint(f.read())

    # you dont have to close the file explicitily 