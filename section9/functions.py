from functools import reduce

def prime(x):
    for i in range(2, x):
        if not x%i:
            return False
    return True

def greater(x,y):
    if x>y:
        return x
    else:
        return y

a = list(map(prime, range(2,156)))
print(a,sep="\n")
b = map(lambda x: x*2, range(6))
print(*b)
c = map(lambda x,y: x>y, range(5), range(5,0, -1))
print(*c)
d = reduce(greater, [5, 7, -6, 56, 12, 75, 65])
print(d)
e = filter(prime, [5, 8, 65, 12, 32, 65])
print(*e)
