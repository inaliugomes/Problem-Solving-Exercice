class EmployeE(object):
    numEmployee = 0
    def __init__(self,name, rate):
        self.owed = 0
        self.name =name
        self.rate = rate
        #numEmployee es un method que pertenece al classe y no al Objeto
        EmployeE.numEmployee += 1

    def delete(self):
        EmployeE.numEmployee -= 1

    def hours(self,numHours):
        self.owed += numHours * self.rate
        return f"{numHours:.2f} hours worth"

    def pay(self):
        self.owed =0
        return f"payed {self.name}"