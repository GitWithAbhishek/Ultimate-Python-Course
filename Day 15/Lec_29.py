# doc String is always written right beolw the function
def square(a):
    '''This Will Make The square Of A Number'''
    return a*a
result = square(5)
print(result)
print(square.__doc__)