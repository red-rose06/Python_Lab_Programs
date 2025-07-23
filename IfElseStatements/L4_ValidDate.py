#Program to check if a date is valid

y = int(input("Enter the year (in numbers): "))
m = int(input("Enter the month (in numbers): "))
d = int(input("Enter the day (in numbers): "))

is_y_valid = "invalid"
is_m_valid = "invalid"
is_d_valid = "invalid"

if(y>0 and y<10000):
    is_y_valid = "valid"
if(m>0 and m<=12):
    is_m_valid = "valid"
if((y%4==0 and y%100!=0)or(y%400==0)):
    if(m==2 and (d>0 and d<=29)):
        is_d_valid = "valid"
elif(m==2):
        if(d>0 and d<=28):
            is_d_valid = "valid"
if m in [1, 3, 5, 7, 8, 10, 12]:
    if(d>0 and d<=31):
        is_d_valid = "valid"
else:
    if(m!=2 and d>0 and d<=30):
        is_d_valid = "valid"

if(is_y_valid=="valid" and is_m_valid=="valid" and is_d_valid=="valid"):
    print("Given date is valid.")
else:
    print("Given date is invalid.")