def greet(fx):
    def mfx():
        print("Hello Every One")
        fx()
        print("Thank You")
    return mfx
@greet
def say():
    print("Good Morning")
say()
