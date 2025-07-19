'''A timestamp is three numbers: a number of hours, minutes and seconds.
Given two timestamps, calculate how many seconds are between them.
The moment of the first timestamp occurred before the moment of the second timestamp.'''

print("Enter details for timestamp 1:- ")
h1 = int(input("Enter no of hours: "))
m1 = int(input("Enter no of minutes: "))
s1 = int(input("Enter no of seconds: "))

print("Enter details for timestamp 2:- ")
h2 = int(input("Enter no of hours: "))
m2 = int(input("Enter no of minutes: "))
s2 = int(input("Enter no of seconds: "))

print("Given:")
print(f"Timestamp 1: {h1}hr {m1}min {s1}s")
print(f"Timestamp 2: {h2}hr {m2}min {s2}s")

seconds1 = 3600*h1 + 60*m1 + s1
seconds2 = 3600*h2 + 60*m2 + s2

diff = seconds2-seconds1

print(f"The number of seconds that occured between the two timestamps is: {diff}s")