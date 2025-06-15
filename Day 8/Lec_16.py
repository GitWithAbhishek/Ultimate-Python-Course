# Indentation is not proper because it is new in python
print("Match Statement in Python")

# Take input and convert it to an integer
a = int(input("Enter A Number: "))

# Match statement begins
match a:
    case 1:print("One")
    case 2:print("Two")
    case _:print("Default")  # Executed when input is not 1 or 2
