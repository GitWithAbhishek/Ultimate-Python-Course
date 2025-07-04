from functools import reduce

def red_fn(x,y):
    return x+y

list1 = [1,2,3,4,5]
ans = reduce(red_fn,list1)
print(ans)

# Example with Lambda Function
ans = reduce(lambda x ,y : x+y+2,list1)
print(ans)