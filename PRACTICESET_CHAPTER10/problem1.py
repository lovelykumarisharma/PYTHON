class programmer:
    company = "microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = programmer("harry",1400000, 19775)
print(p.name, p.salary, p.pin, p.company)