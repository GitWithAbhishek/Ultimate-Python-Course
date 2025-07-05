import random as r
list1 = ["snake","water","gun"]
a = r.choice(list1)
inpt = input("Enter Your Choice : ")
if(a == inpt):
    print("Draw")
elif(a == "snake" and inpt == "water"):
    print("Loss")
elif(a == "snake" and inpt == "gun"):
    print("Win")
elif(a == "water" and inpt == "gun"):
    print("Loss")
elif(a == "water" and inpt == "snake"):
    print("Win")
elif(a == "gun" and inpt == "water"):
    print("Win")
elif(a == "gun" and inpt == "snake"):
    print("Loss")

