with open("practiceSET_chaper9/old.txt") as f:
    content = f.read()

with open("practiceSET_chaper9/mynewfile.txt", "w") as f:
    f.write(content)