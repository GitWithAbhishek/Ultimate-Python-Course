print("Operation On Tuples")

# We Can not directly change the tuple but we can convert in into list then we can perform changes then again convert back to tuple
tup = (0,1,2,3,4)
lst = list(tup)
lst.append(5)
lst.remove(0)
tup = tuple(lst)
print(tup)

# We Can Concatinate two tuple simply
tup1 = ("Aman" ,"Pandey")
tup2 = ("Naman" , "Pandey")
tup3 = tup1 + tup2
print(tup3)

# Count
tupcount = (1,2,2,2,2,2,3,4,5,6,7,8,10)
print(tupcount.count(2))

# Index
print(tupcount.index(2))
print(tupcount.index(2,4,8))  # value , start , end