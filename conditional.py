a = int(input("Enter your age :"))
print("Your age is :", a)
if(a>18):
    print("You can drive")
elif(a==18):
    print("You can drive")
else:
    print("You cannot drive")


 # Nested if conditional
num = 34
if(num < 0):
    print("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num  > 10 and num<= 20 ):
        print("Number is beteen 11-20")
    else:
        print("Number is greater than 20")