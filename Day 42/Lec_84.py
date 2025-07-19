import time
# def whileLoop():
#     i=0
#     while i<500:
#         print(i)
#         i=i+1
# def forLoop():
#     for i in range (500):
#         print(i)
# samay = time.time()
# whileLoop()
# t1=time.time()-samay
# print(t1)
# forLoop()
# print(time.time()-samay)


# Part Two Of Code 
# time.sleep(3)
# print("This Will Print after 3 second")

# Part Three of code
t=time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)
