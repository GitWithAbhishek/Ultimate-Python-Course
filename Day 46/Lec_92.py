from functools import lru_cache
import time
@lru_cache(maxsize=None)
def funX(n):
    time.sleep(3)
    return n*10

print(funX(10))
print("Done for 10")
print(funX(20))
print("Done for 20")
print(funX(30))
print("Done for 30")

# Now We Are Repeating The Values But They Are Going To Be Return At Once Because The Value Is Already Stored

print(funX(10))
print("Done for 10")
print(funX(20))
print("Done for 20")
print(funX(30))
print("Done for 30")

# Giving New Value It Will Take Time To Compute It
print(funX(40))
print("Done for 40")