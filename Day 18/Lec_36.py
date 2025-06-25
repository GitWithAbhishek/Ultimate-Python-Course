print("Exception Handling")

a = input("Enter A Number : ")
print(f"We Are going to print table of {a}")

try:
    for i in range (1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print("Some Error Occured ",e)

