def commonMultiple(x, y):
    least = 0
    while True:
        for i in range(len(x)): #x>y
            for j in range(len(y)):
                if x[i] == y[j]:
                    least = x[i]
                    return least
        x, y = listappend(x, y, 1)

def listappend(x, y, q = 0):
    if q == 0:
        tmpX, tmpY = x, y
        x = list()
        y = list()
        x.append(tmpX)
        y.append(tmpY)
        return x,y
    elif q == 1:
        x.append(x[len(x)-1]+x[0])
        y.append(y[len(y)-1]+y[0])
        return x, y

a = int(input("Enter a number"))
b = int(input("Enter a number"))

a, b = listappend(a, b)

print(commonMultiple(a,b))