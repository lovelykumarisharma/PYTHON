words = ["donkey","bad", "ganda"]

with open("practiceSET_chaper9/file5.txt", "r") as f:
    content = f.read()

for word in words:

    content = content.replace(word, "#"* len(word))

with open("practiceSET_chaper9/file5.txt", "w") as f:
    f.write(content)