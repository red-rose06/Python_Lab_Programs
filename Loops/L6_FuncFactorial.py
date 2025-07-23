#Program of function to print factorial of a number

def factorial(n):
    fact=1

    if(n==0):
        print("Factorial of 0 is 1")
    elif(n<0):
        print(f"Factorial of {n} does not exist")
    else:
        for i in range(2, n+1):
            fact = fact*i
        print(f"The factorial of {n} is {fact}")

factorial(int(input("Enter a number: ")))