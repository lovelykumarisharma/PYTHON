with open("practiceSET_chaper9/log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in lines):
        print(f"yes python is presant. line no: {lineno}")
        break
    lineno += 1

else:
    print("no python is not presant")