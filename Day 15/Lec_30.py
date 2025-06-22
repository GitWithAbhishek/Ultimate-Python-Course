def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    

def fibonnaci(n):
    if n==0 or n==1:
        return 1
    else:
        return (fibonnaci(n-1)+fibonnaci(n-2))
    
result = factorial(5)
print(result)

result2 = fibonnaci(5)
print(result2)