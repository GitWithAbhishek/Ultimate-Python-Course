class Animal:  # Parent class
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
d.sound()  
d.bark()  

c = Cat()
c.sound() 
c.meow()   
