# Fianlly Keyword - It is very useful in case of function where function return anything 
def funct():
    try:
        list=[1,2,3,4,5]
        print("Hello The value is",list[5])
        return 1
    except:
        print("Some error occured")
        return -1
    finally:
        print("This is Finally Block")
funct()