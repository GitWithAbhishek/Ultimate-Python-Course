class Myclass:
    def __init__(self):
        self.__name = "Abhishek"  # __ is the private variable

a = Myclass()
print(a._Myclass__name) # Can be access Indirectly - This is called name mangling