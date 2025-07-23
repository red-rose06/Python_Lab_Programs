#Program to find the sum of numbers of digit recursively

def sum(x):
    if(x<10):
        return x
    else:
        return x%10 + sum(x//10)


n = int(input("Enter a number: "))

if(n<0):
    print("Please enter a positive number")
if(n==0):
    print("Sum is 0")
else:
    print(sum(n))