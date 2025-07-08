class Vechile:
    def horn(self):
        print("POOO POOO")
    def light(self):
        print("Blow")
class bike(Vechile):
    def wheels(self):
        print("Two")
a = Vechile()
b=bike()
a.horn()
a.light()
b.wheels()