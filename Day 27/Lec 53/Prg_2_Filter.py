def filter_fun(a):
    return a>5
list1 = [1,2,3,4,5,6,7,8,9,10]
ans = list(filter(filter_fun,list1))
print(ans)

# Example With Lambda Function
list2 = [1,2,3,4,5,6,7,8,9,10]
ans2 = list(filter(lambda x:x>5,list1))
print(ans2)