'''Program to find maximum of three numbers'''
#Using logical operators

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
c = float(input("Enter the third number (c): "))

print(f"a = {a}, b = {b}, c = {c}")

if((a>b and a>c)or(a==b and a>c)or(a==c and a>b)):      #you may or may not use paranthesis
    print(f"{a} is the largest number")
elif((b>a and b>c)or(b==c and b>a)):
    print(f"{b} is the largest number")
elif(c>a and c>b):
    print(f"{c} is the largest number")
else:
    print("All numbers are equal")
