print("Intro To Dicitionary")

dict1 = {1:"Aman",2:"Naman",3:"Hari"}
print(dict1)

print(dict1[2])
print(dict1.get(1)) # It Will Not Throw Error

print(dict1.keys())
print(dict1.values())
print(dict1.items())

for i in dict1.keys():
    print(f"The Value Corresponding to {i} is", dict1[i])

for key,value in dict1.items():
    print(f"The Value Corresponding to {key} is {value}")