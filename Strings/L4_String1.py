'''Given a string.
Delete from it all characters whose indices are divisible by 3.'''

#Method 1

s1 = "abcdefghijk"

s2 = s1[:3]+s1[4:6]+s1[7:9]+s1[9:]

print("Edited string is ", s2)

