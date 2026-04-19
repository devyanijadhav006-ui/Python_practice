import datetime
#get the current hour
currentTime= datetime.datetime.now().hour

if currentTime<12:
    print("Good Morning!")
elif currentTime<18:
    print("Good Afternoon!")
else:
    print("Good evening!")

#USING time MODULE::
import time

currentTime= time.localtime().tm_hour
if currentTime<12:
    print("Good Morning!")
elif currentTime<18:
    print("Good Afternoon!")
else:
    print("Good evening!")


