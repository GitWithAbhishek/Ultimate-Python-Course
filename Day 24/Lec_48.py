x = 4
y = 6
print(x)

def printvalue():
    x=6
    global y
    y=10
    print(x)

printvalue();
print(y)