class Mobile:
    Company = "Samsung"
    def __init__(self,model,price):
        self.model = model
        self.price = price
        
    def showDetails(self):
        print(f"Mobile Comapny is {self.Company} and model is {self.model} in {self.price}")    
mob1 = Mobile("S23","30K")
mob2 = Mobile("Iphone","80K")
mob2.Company = "Apple"
mob3 = Mobile("S24 Ultra","1 Lac 30k")
mob1.showDetails()
mob2.showDetails()
mob3.showDetails()
