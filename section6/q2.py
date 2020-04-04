## Long solution -----------------------------------------------------------
def aliquot(x):
    ls = list()
    for i in range(1, x+1):
        if not x%i:
            ls.append(i)
    return ls

def greatestCommonDivisor(x, y):
    great = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                if x[i] > great:
                    great = x[i]
    return great
##--------------------------------------------------------------------------
## Small solution-----------------------------------------------------------
def commonDivisor(x, y):
    for i in range(x, 0, -1):
        for j in range(y, 0, -1):
            if (not x%i) and (not y%i):
                return i
##--------------------------------------------------------------------------

a = int(input("Please enter number"))
b = int(input("Please enter number"))

print(greatestCommonDivisor(aliquot(a), aliquot(b)))    ##Long

print(commonDivisor(a, b))                              ##Small