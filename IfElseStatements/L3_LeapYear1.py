'''Program to check whether the entered number is a leap year or not'''
#Using operators

yr = int(input("Enter the year: "))

if((yr%4 == 0)and(yr%100 != 0)):
    print(f"{yr} is a leap year")
elif((yr%4 == 0 )and(yr%100 == 0)and(yr%400 == 0)):
    print(f"{yr} is a leap year")
else:
    print(f"{yr} is not a leap year")