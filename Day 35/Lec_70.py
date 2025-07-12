class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromstr(cls,stri):
        return cls(stri.split("-")[0],stri.split("-")[1])
    def show(self):
        print(f"The Employee Name Is {self.name} And Salary Is {self.salary}")
str1 = "Aman-12000"
e1 = Employee("Harry",120000)
e1.show()
e2 = Employee.fromstr(str1)
e2.show()