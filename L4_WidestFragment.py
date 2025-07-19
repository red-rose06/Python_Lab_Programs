"""Given a sequence of integer numbers ending with the number 0.
Determine the length of the widest fragment where all the elements are equal to each other."""

n = []

#Input list
num=1
while num!=0:
    num=int(input("Enter a number. Enter 0 to stop: "))
    n.append(num)

print(f"Entered list is {n}")

l=0
l_max=0
t=n[0]
i=0

while t!=0:
    
    while t==n[i]:
        if(t==n[i]):
            l=l+1
        i=i+1

    if l>l_max:
        l_max = l
    t=n[i]
    l=0

print(f"Widest fragment is {l_max}")