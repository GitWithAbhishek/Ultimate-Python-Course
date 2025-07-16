class Calculator:
    def add(self, *numbers):
        print("Sum is:", sum(numbers))

c = Calculator()
c.add(2, 3)
c.add(1, 2, 3, 4)
