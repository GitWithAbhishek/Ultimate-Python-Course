# Base class
class Animal:
    def sound(self):
        print("Animals make different sounds")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

class Pet(Dog, Cat):
    def pet_info(self):
        print("This is a pet animal")

p = Pet()

p.sound()  
p.bark()      
p.meow()      
p.pet_info()    
