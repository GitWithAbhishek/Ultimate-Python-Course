class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.version = 1
p = Person("Aman",12)
print(p.__dict__)
print(help(Person))