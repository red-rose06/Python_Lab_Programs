#3. Program to print Factorial of a number

n = int(input("Enter a number: "))

fact = 1

if n<0:
    print(f"Factorial of {n} does not exist.")
elif n==0:
    print(f"Factorial of {n} is 1.")
else:
    for i in range(1,n+1):
        fact = fact * i
    print(f"Factorial of {n} is {fact}.")

'''or simply import math module and use math.factorial(n)
you can use 'm' instead of 'math' by using aliasing
import math as m'''