class Myclass:
    def __init__(self, value):
        self._value = value

    @property
    def ten_value(self):
        return self._value

    @ten_value.setter   # Setter Method
    def ten_value(self, new_val):
        self._value = new_val

obj = Myclass(10)
obj.ten_value = 90
print(obj._value)
