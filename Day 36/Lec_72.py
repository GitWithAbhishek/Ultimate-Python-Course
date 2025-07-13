class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Programmer(Employee):
    def __init__(self, name, id,lang):
        super().__init__(name, id)
        self.lang = lang
Aman = Programmer("Aman",123,"JAVA")
print(Aman.name)
print(Aman.id)
print(Aman.lang)
        