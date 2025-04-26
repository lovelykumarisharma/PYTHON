f = open("practiceSET_chaper9/poem.txt")
content = f.read()
if("twickle" in content):
    print("the word twinckle is present in the content")

else:
    print("the word twinckle is not  present in the content")

f.close()