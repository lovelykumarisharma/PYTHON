with open("practiceSET_chaper9/file12.txt") as f:
    content1 = f.read()

with open("practiceSET_chaper9/poem.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("print yes these are identical")

else:
    print(" no this file is not identical!")