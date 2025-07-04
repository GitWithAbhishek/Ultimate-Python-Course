def cube(x):
    return x*x*x
list1 = [1,2,3,4,5,6,7,8,9,10]
ans = list(map(cube,list1))
print(ans)

# Example with Lambda Function

list2 = [11,12,123,231,23,3,54]
ans2 = list(map(lambda x : x*x*x,list2))
print(ans2)