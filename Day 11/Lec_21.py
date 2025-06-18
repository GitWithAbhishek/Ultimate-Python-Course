# Required Arguments
def average(a,b):
    print("The Average Is ",(a+b)/2)

average(4,6)

# Deafult Arguments
def perimeter(a=2,b=2):
    print("Perimeter is ",a+b)

perimeter(5)

# Keyword Argument

def name(fname,mname,lname):
    print("My Name is ",fname,mname,lname)

name(lname="Pandey",fname="Aman",mname="Narayan")

# Keyword Arbitary Arguments

def sum(*num):
    sum=0
    for i in num:
        sum = sum+i
    print("The Sum Is ",sum)

sum(1,2,3,4,5,6,7,8,9,10)

# Return Statement

def retsum(a,b):
    return a+b

result = retsum(1,2)
print("The Return Value Is ",result)