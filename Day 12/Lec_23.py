print("List Methods")

list1 = [10,9,8,7,6,5,4,3,2]

list1.append(1)
print(list1)

list1.insert(0,0)
print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list2 = [1,1,1,2,3,1,12,4,5,1]
print(list2.count(1))
print(list2.index(2))

# importance of copy function in python list
list3 = [1,2,3,4,5]
m=list3 # This will act as a refrence
m[0]=0  # Value Change occur in original list
print(list3) 

# To Overcome this we use copy method in python
list4 = [1,2,3,4,5,6]
n = list4.copy()
n[0]=0
print(list4)
print(n)

list5 = [11,12,13,14,15]
list4.extend(list5)
print(list4)

lst = list4 + list5
print(lst)