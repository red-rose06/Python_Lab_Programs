#2. Program to print Multiplication table of any number

n = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")