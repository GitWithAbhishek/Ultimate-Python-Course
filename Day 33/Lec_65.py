print("Static Method In Python")
class Myclass:
    def __init__(self,n):
        self.num = n
    @staticmethod # No need to use self with static functions And There Is No Need To Create An Object
    def myfun(a,b):
        return a+b
obj = Myclass(5)
print(obj.num)
print(obj.myfun(5,6))
print(Myclass.myfun(4,6))