'''Program to find maximum of three numbers'''
#Without using logical operators

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
c = float(input("Enter the third number (c): "))

print(f"a = {a}, b = {b}, c = {c}")

if(a>b):
    if((a>c)or(a==c)):
        print(f"{a} is the largest number.")
    else:
        print(f"{c} is the largest number.")
elif(b>c):
    if((b>a)or(b==a)):
        print(f"{b} is the largest number.")
    else:
        print(f"{a} is the largest number.")
elif(c>a):
    if((c>b)or(c==b)):
        print(f"{c} is the largest number.")
    else:
        print(f"{b} is the largest number.")
else:
    print("All numbers are equal.")
