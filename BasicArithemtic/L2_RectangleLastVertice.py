'''Input 3 vertices of a rectangle whose sides are parallel to the coordinate axes and find the 4th one.'''

print("Enter the vertices of a rectange whose sides are parallel to the coordinate axes.")

ax = int(input("Enter x-coordinate of vertex A: "))
ay = int(input("Enter y-coordinate of vertex A: "))

bx = int(input("Enter x-coordinate of vertex B: "))
by = int(input("Enter y-coordinate of vertex B: "))

cx = int(input("Enter x-coordinate of vertex C: "))
cy = int(input("Enter y-coordinate of vertex C: "))

dx = cx
dy = by

print(f"Vertex A: {(ax, ay)}")
print(f"Vertex B: {(bx, by)}")
print(f"Vertex C: {(cx, cy)}")
print(f"Vertex D: {(dx, dy)}")
