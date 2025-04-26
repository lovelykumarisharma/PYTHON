word = "donkey"

with open("practiceSET_chaper9/file12.txt") as f:
    content = f.read()

contentnew = content.replace(word, "#####")

with open("practiceSET_chaper9/file12.txt", "w") as f:
    f.write(contentnew)