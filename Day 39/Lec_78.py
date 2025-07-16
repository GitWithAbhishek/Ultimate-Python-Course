class Animal:
    def __init__(self, nofeet, behaviour):
        self.nofeet = nofeet
        self.behaviour = behaviour

    def show_details(self):
        print(f"No of Feet: {self.nofeet}")
        print(f"Behaviour: {self.behaviour}")

class Cat(Animal):  # Single Inheritance
    def __init__(self, nofeet, behaviour, sound):
        super().__init__(nofeet, behaviour)  # Inherit from Animal
        self.sound = sound

    def show_cat_details(self):
        self.show_details()  # Call Animal's method
        print(f"Sound: {self.sound}")

# Create object of Cat (child class)
billi = Cat("4", "Pet", "Meow Meow")

# Call child class method
billi.show_cat_details()
