print("Intro To Tuple")

tup = (1,2,3,4,5,"Aman","Naman")
print(type(tup),tup)

tup2 = (1) #This Type is <int>
print(type(tup2))

tup3 = (1,) #This Type is <tuple>
print(type(tup3))

if "Aman" in tup:
    print("Yes")
else:
    print("No")

print(tup[:])
print(tup[:-3])