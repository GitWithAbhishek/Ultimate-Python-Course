print("If Else Conditional Statement")

age = int(input("Enter Your Age : "))
if(age<4):
    print("Go To Playgrarden");
elif(age >=4 and age<18):
    print("Go To School")
elif(age>=18 and age<25):
    print("Go To College")
elif(age>=25 and age<65):
    print("Go To Job")
else:
    print("Get Retirment")