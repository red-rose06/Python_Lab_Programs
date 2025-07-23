#Program to display a number in reverse order

num = int(input("Enter a number: "))

n = num
nReverse = 0

while n>0:
    nReverse = nReverse*(10)+n%10
    n = n//10

print(f"Reversed number of {num} is {nReverse}")