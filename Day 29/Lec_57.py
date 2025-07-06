class Bike:
    name = "Apache"
    brand = "TVS"
    price = "Two Lakh"
    def details(self):
        print(f"Bike Name Is {self.name} And Brand Is {self.brand} And The Price is {self.price}")

a = Bike() # No Need To Use New Keyword Like Java
print(a.name)
a.details()

b = Bike()
b.name = "Raider"
b.price = "One Lakh"
b.details() # It Will Take Brand As Deafult