class Person:

    def __init__(self,name,idNumber):
        self.name= name
        self.idNumber = idNumber
    
    def display(self):
        print(f"{self.name} ID: {self.idNumber}")
       

class Employee(Person):
    def __init__(self, name, idNumber,salary,post):
        super().__init__(name, idNumber)
        self.salary = salary
        self.post =post


    def dispaly(self):
         print(f"Name: {self.name} \nID: {self.idNumber} \nPost: {self.post}\nSalary: {self.salary}")

a = Employee('Rahul', 93886012, 20000, "Intern")

a.dispaly()