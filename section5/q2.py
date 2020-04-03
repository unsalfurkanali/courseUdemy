x = int(input("Please enter a number"))
divider = 1
for i in range(2, x):
    if not (x%i):
        divider = divider + i

if divider == x:
    print("{} is a perfect number!".format(x))