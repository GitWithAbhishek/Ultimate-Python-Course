# Introduction to list

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = ["Aman","Naman","Gaurav","Yash","Udit"]
list3 = [1,2,3,4,5,"Naman","Gaurav","Yash","Udit"]

print(list1)
print(list2)
print(list3)

print(list3[:]) #Commplete List will Print
print(list3[2:5])
print(list3[0::2])

print(list1[2])
print(list2[-3])

if "Gaurav" in list2:
    print("Yes")
else:
    print("No")


# List compherssion
list4 = ["Aman","Abhishek","Naman","Yash","Udit","Gaurav","Ankit","Rahul"]
lst = [i for i in list4 if "a" in i]
print("List Compherssion Result ",lst)