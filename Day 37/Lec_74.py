class Parent:
    def show(self):
        print("This is the parent class")

class Child(Parent):
    def show(self):  # Overriding the parent method
        print("This is the child class")

# Create objects
p = Parent()
c = Child()

p.show()  # Output: This is the parent class
c.show()  # Output: This is the child class (overridden)
