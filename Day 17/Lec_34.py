print("Dicitionary Methods")

dict1 = {1:"Aman",2:"Naman",3:"Hari"}
dict2 = {5:"Pandey",6:"Raj"}

# Update
dict1.update({4:"Narayan"})
dict1.update(dict2)
print(dict1)

# Clear
dict2.clear()
print(dict2)

# Pop - Remove sepific key value pair
dict1.pop(2)
print(dict1)

# Pop Item - Remove Last Key Value pair
dict1.popitem()
print(dict1)

# Del 
del dict2