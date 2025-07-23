'''A school decided to replace the seks in three classrooms.
Each desk sits two students.
Given: no of students in each class.
Print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.'''

a = int(input("Enter the number of students in the first class: "))
b = int(input("Enter the number of students in the second class: "))
c = int(input("Enter the number of students in the third class: "))

benchesA = a//2 + a%2
benchesB = b//2 + b%2
benchesC = c//2 + c%2

print(f"The minimum number of benches required are {benchesA+benchesB+benchesC}")