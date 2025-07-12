class car:
    company = "Toyota"
    def show(self):
        print(f"The Car Name is {self.name} And The Brand Is {self.company}")
    @classmethod
    def changeName(cls,newcompany):
        cls.company = newcompany
e1 = car()
e1.name = "sfddf"
e1.show()
e1.changeName("TVS")
e1.show()