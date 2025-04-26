class employee:
    language = "python" # this is class attribute
    salary = 1200000

    def getinfo(self): #function 
        print(f"the language is {self.language}. the salary is{self.salary}")


    @staticmethod #great ek static method h or usko object ki jarurt nhi h
    def great():
        print("good morning")


harry = employee()
harry.language = "javaScript"


# here name is object attribute ans salary and language are the clas atribute as they directly blong to clss

harry.getinfo()
harry.great()
# employee.getinfo(harry)