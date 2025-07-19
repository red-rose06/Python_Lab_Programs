#Function to print maximum of two numbers

def max(a,b):
    if(a>b):
        print(f"{a} is greater than {b}")
    elif(a<b):
        print(f"{b} is greater than {a}")
    else:
        print("Both are equal")

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
max(n1, n2)