print("Methods In Sets")

s1 = {1,2,3,4}
s2 = {3,4,5,6,7}

# UNION OPERATION
s3 = s1.union(s2)
print(s3)

# UPDATE OPERATION
s1.update(s2)
print(s1)

s1 = {1,2,3,4}
s2 = {3,4,5,6,7}

# INTERSECTION OPERATION
s3 = s1.intersection(s2)
print(s3)

# INTERSECTION UPDATE
s1.intersection_update(s2)
print(s1)

cities1 = {"Lucknow","Kanpur","Delhi","Noida"}
cities2 = {"Jabalpur","Bhopal","Lucknow","Delhi"}

# Symmertic Difference
cities = cities1.symmetric_difference(cities2)
print(cities)

# Diffference
cities = cities1.difference(cities2)
print(cities)

# Isdisjoint
print(cities1.isdisjoint(cities2))

set1 = {1,2,3,4,5}
set2 = {2,3}
# Superset
print(set1.issuperset(set2))
# Subset
print(set2.issubset(set1))

city = {"Lucknow","Kanpur"}
# Add One Item Use ADD
city.add("Delhi")
# Delete One Item Use Remove - It Will Throw An error If The Item Is Not Present In SET
city.remove("Kanpur")
print(city)

# Delete One Item Use Discard - It Will Not Throw An error If The Item Is Not Present In SET
city.discard("Ajmer")  # Ajmer Is Not Present In the Set

# POP Operation - It Will Remove Random Item And You Can Access
print(city.pop())

# DELETE OPERATION - It WIll Delete Whole Set
del city

# CLEAR OPERATION - It Will Remove Whole Items
set1.clear()
