#Program to create and view elements of a list


a = []

limit = int(input("Enter number of elements: "))

for i in range(0,limit):
    a.append(int(input(f"Enter list element {i}: ")))

print("The entered list is: ")

for i in range(0,limit):
    print(f"{a[i]}  ")