class Grandfather:
    def show_grandfather(self):
        print("This is the Grandfather class")

class Father(Grandfather):
    def show_father(self):
        print("This is the Father class")

class Child(Father):
    def show_child(self):
        print("This is the Child class")

c = Child()

c.show_grandfather()
c.show_father()
c.show_child()
