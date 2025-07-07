def greet(fx):
    def mfx(*args,**kwargs):
        print("Hello Every One")
        fx(*args,**kwargs)
        print("Thank You")
    return mfx
@greet
def add(a,b):
    c=a+b
    print("The Sum Is ",c)
add(10,17)
