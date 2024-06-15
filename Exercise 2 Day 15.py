import time
timestamp = time.strftime('%H:%M:%S')
print("Time : " + timestamp)
if(int(time.strftime('%H')) < 12 ):
    print("Good Morning")
elif(int(time.strftime('%H')) >= 12 and int(time.strftime('%H')) <= 15):
    print("Good Afernoon")
elif(int(time.strftime('%H')) >= 15 and int(time.strftime('%H')) <= 19):
    print("Good Evening")
else:
    print("Good Night")


