#Program to check whether a number is prime

n = int(input("Enter a number: "))

if n<=0 or n==1:
    print(f"{n} is neither prime nor composite.")
elif n==2:
    print(f"{n} is a prime number")
else:
    flag = 0
    for i in range(2,n):
        if n%i==0:
            flag = 1
    if flag==0:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is a composite number")