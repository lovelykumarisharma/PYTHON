with open("practiceSET_chaper9/this.txt") as f:
    content = f.read()

with open("practiceSET_chaper9/this_copy.txt", "w") as f:
    content = f.write(content)