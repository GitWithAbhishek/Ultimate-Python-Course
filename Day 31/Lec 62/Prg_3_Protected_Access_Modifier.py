class Myclass:
    def __init__(self):
        self._name = "Abhishek"  # _ is the protected variable

a = Myclass()
print(a._name) 