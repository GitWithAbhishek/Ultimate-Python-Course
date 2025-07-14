class Employee:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return (f"Hello I Am STR {self.name}")
    def __call__(self):
        print("Hello")
    def __repr__(self):
        return(f"My Name is {self.name}")

Aman = Employee("Aman")
print(str(Aman))
print(repr(Aman))
Aman()