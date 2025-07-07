# Getter Function In Python
class Myclass:
    def __init__(self,value):
        self._value = value
    @property
    def showtenx(self):
        return self._value*10
a= Myclass(10)
print(a.showtenx)