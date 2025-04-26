class employee:
    language = "python" # this is class attribute
    salary = 1200000

    def __init__(self,name ,salary ,language): #donder method which is automattically called
        self.name = name
        self.salary = salary
        self.language = language
        print(" i am creating an object")

    def getinfo(self): #function 
        print(f"the language is {self.language}. the salary is{self.salary}")


    @staticmethod #great ek static method h or usko object ki jarurt nhi h
    def great():
        print("good morning")


harry = employee("hary",1300000, "javascript")
harry.name = "harry"
print(harry.language,harry.salary)

rohan = employee("rohan", 1400000,"java")