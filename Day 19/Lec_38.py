# Raising Custom Error
a = int(input("Enter Salary Between 5000 to 50000 :- "))

if (a<500 or a>50000):
    raise ValueError("Salary Is Inappropriate")