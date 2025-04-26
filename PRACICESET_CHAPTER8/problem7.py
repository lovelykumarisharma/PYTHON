def remove(l,word):

    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    # for item in l:
    #     l.remove(word)
    return n

l = ["harry", "rohan", "shubham", "an"]

print(remove(l, "an"))


