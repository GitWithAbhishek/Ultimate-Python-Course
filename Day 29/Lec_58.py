class car:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand
    def info(self):
        print(f"Car Name Is {self.name} And Brand Is {self.brand}")
a = car("Fortuner","Toyota")
b = car("B6e","Mahindra")
a.info()
b.info()