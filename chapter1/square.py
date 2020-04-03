import math as mt
x = 0
y = 0
points = [[float(input("x1 ")), float(input("y1 "))], [float(input("x2 ")), float(input("y2 "))], [float(input("x3 ")), float(input("y3 "))], [float(input("x4 ")), float(input("y4 "))]]

if points[0][0] == points[1][0]:
    x = x + 1
if points[0][1] == points[1][1]:
    y = y + 1
for j in range(2, 4, 1):
    for i in range(0, 3, 1):
        if i != j:
            if points[i][0] == points[j][0]:
                x = x + 1
            if points[i][1] == points[j][1]:
                y = y + 1

a = round(mt.sqrt((points[1][0]-points[0][0])**2 + (points[1][1]-points[0][1])**2), 3)
b = round(mt.sqrt((points[2][0]-points[3][0])**2 + (points[2][1]-points[3][1])**2), 3)
c = round(mt.sqrt((points[0][0]-points[2][0])**2 + (points[0][1]-points[2][1])**2), 3)
d = round(mt.sqrt((points[1][0]-points[3][0])**2 + (points[1][1]-points[3][1])**2), 3)
e = round(mt.sqrt((points[0][0]-points[3][0])**2 + (points[0][1]-points[3][1])**2), 3)
f = round(mt.sqrt((points[1][0]-points[2][0])**2 + (points[1][1]-points[2][1])**2), 3)
g = round(mt.sqrt((points[0][0]-points[1][0])**2 + (points[0][1]-points[1][1])**2), 3)
h = round(mt.sqrt((points[2][0]-points[3][0])**2 + (points[2][1]-points[3][1])**2), 3)

if ((a == b and c == d) or (e == f and g == h)):
    print("It is a rectangle")
