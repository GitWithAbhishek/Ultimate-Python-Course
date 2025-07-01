# Encryption Or Decryption Program
import random
import string
b = input("Select E For Encryption Or D For Decryption : ")
if b == 'E':
    a = input("Enter The String ")
    if len(a) >=3:
        c= a[0]
        a=a[1:]
        a=a+c
        random_string = ''.join(random.choices(string.ascii_letters, k=3))
        a=random_string+a
        a=a+random_string
        print(a)
    else:
        a=a[::-1]
        print(a)
if b == 'D':
    a = input("Enter The String ")
    if len(a) >=3:
        a= a[3:-3]
        c=a[len(a)-1:]
        a=c+a
        a=a[:-1]
        print(a)
    else:
        a=a[::-1]
        print(a)
