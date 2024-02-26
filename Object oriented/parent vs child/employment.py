class Employees:
    def __init__(self,name,last) -> None:
        self.name =name
        self.last =last
        pass

class Supervisor(Employees):
    def __init__(self, name, last,password) -> None:
        super().__init__(name, last)
        self.password= password

class Chefs(Employees):
    def leave_request(self,days):
        return f"May I take leave for {days} days"
    

adrian = Supervisor("Adrian","A","apple")
emily = Chefs("Emily","E")
juno = Chefs("Juno","J")

print(emily.name)
print(emily.leave_request(4))
print(juno.name,"",juno.last)