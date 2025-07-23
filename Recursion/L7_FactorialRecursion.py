#Program to find factorial of a number using recursion

def fact(x):
    if (x==1):
        return 1
    if (x>1):
        return x*fact(x-1)


n = int(input("Enter a number: "))

if(n<0):
    print(f"Factorial of {n} does not exist")
elif(n==0):
    print("Factorial of 0 is 1")
else:
    print(f"Factorial of number is ", fact(n))