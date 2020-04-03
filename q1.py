x = input("Please enter a number")
power = 0

for i in x:
    power = int(i)**len(x) + power

if int(x) == power:
    print("Excellent! {} is a Amstrong Number".format(x))

