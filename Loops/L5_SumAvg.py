#Program to calculate sum and average of first n numbers

limit = int(input("Enter the limit of numbers: "))

sum = 0

for i in range(0,limit):
    n = float(input("Enter a number: "))
    sum = sum + n

avg = sum/limit

print(f"Sum is {round(sum,2)} and average is {round(avg,2)}")