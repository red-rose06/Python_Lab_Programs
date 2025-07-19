'''Given a string.
Delete from it all characters whose indices are divisible by 3.'''

#Method 3

s1 = list(input("Enter a string: "))

i = 0
s2 = ['']
j = 0

for i  in range(0,len(s1)-1):
    if i%3==0:
        s2[j] = s1[i]
        j+=1
    i+=1


print("New string: ", "".join(s2))