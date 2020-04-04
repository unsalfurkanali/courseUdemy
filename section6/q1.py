## Long solution -----------------------------------------------------------
def aliq(x):
    aliqls = list()
    for i in range(1, x):
        if not x%i:
            aliqls.append(i)
    return aliqls

def sum(x):
    total = 0
    for i in range(len(x)):
        total += x[i]
    return total

perf = lambda x,y : x==y

##--------------------------------------------------------------------------
## Small solution-----------------------------------------------------------
def perfectNumber(x):
    sum = 0
    for i in range(1, x):
        if not x%i:
            sum += i
    if sum == x:
        return True
    else:
        return False
##--------------------------------------------------------------------------

for i in range(1, 1000):
    if perf(i, sum(aliq(i))):       ##Long way
        print(i)
    if perfectNumber(i):            ##Small way
        print(i)        