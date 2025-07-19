'''Program to give roots of a quadratic equation'''

import math

print("Enter the equation: ax2 + bx + c : ")

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

print(f"Given equation is {a}x2 + {b}x + {c}")

if(b*b>=4*a*c):
    D = math.sqrt(b*b - 4*a*c)
    x1 = (-b + D)/(2*a)
    x2 = (-b - D)/(2*a)
    print(f"The roots of the equation are {x1} and {x2}.")
else:
    print(f"The equation has complex roots.")