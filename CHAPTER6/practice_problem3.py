p1 = 'make a lot of money'
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
massage = input("Enter your comment: ")

if((p1 in massage) or (p2 in massage) or( p3 in massage) or (p4 in massage)):
    print("this ocmment is spam")

else:
    print("comment is not spam")