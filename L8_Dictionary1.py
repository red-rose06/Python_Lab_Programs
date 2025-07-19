#Create and print a dictionary keys, values and key-value pairs

d = {'a':354, 'b': "Second", 'c': 874}

print(d.keys())
print(d.values())
print(d.items())

d['a']=56
d['b']="Updated"

print(d.keys())
print(d.values())
print(d.items())

d["ar"]=10
print(d.items())


d["ar"]=11
print(d.items())

k = input("Enter a key: ")
val = input("Enter a value: ")

d[k]=val
print(d.items())