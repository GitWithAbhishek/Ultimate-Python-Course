# Greet Exercise
import time
timevar= time.strftime('%H:%M:%S')
print(timevar)
if(timevar>'00:00:00' and timevar<'12:00:00'):
    print("Good Morning")
elif(timevar>='12:00:00' and timevar<'18:00:00'):
    print("Good Evening")
else:
    print("Good Night")