import time
import threading

def fun(second):
    print(f"Sleeping for {second} seconds")
    time.sleep(second)

time1 = time.perf_counter()

t1=threading.Thread(target=fun, args=[4])
t2=threading.Thread(target=fun, args=[2])
t3=threading.Thread(target=fun, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
print(f"Time taken: {time2 - time1} seconds")