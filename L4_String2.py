'''Given a string.
Delete from it all characters whose indices are divisible by 3.'''

#Method 2

s1 = list(input("Enter a string: "))

del s1[3::3]

print("Updated string is: ", s1)  #List

s2 = "".join(s1)

print("Updated string is: ", s2)  #String




