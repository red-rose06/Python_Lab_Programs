'''Take input of hours, minutes and seconds. Find the angle of the hour hand wrt midnight.'''

H = int(input("Enter number of hours between 0 and 12: "))
M = int(input("Enter number of minutes between 0 and 60: "))
S = int(input("Enter number of seconds between 0 and 60: "))

angle = H*30 + M*0.5

print(f"The angle of the hour hand is {angle} degrees.")