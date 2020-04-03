import math as mt

points = [[float(input("x1 ")), float(input("y1 "))], [float(input("x2 ")), float(input("y2 "))], [float(input("x3 ")), float(input("y3 "))]]

a = round(mt.sqrt((points[1][0]-points[0][0])**2 + (points[1][1]-points[0][1])**2), 3)
b = round(mt.sqrt((points[2][0]-points[0][0])**2 + (points[2][1]-points[0][1])**2), 3)
c = round(mt.sqrt((points[2][0]-points[1][0])**2 + (points[2][1]-points[1][1])**2), 3)
print("a = ", a)
print("b = ", b)
print("c = ", c)

if abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c < a+b:
    if a == b and a == c:
        print("Eşkenar Üçgen")
    elif a == b or a == c:
        print("İkizkenar Üçgen")
    else:
        print("Üçgen")
else:
    print("Bu koordinatlar bir üçgen belirtmiyor.")