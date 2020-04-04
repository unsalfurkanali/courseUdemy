def aliq(x):
    ls = list()
    for i in range(1, x):
        if not x%i:
            ls.append(i)
    return ls


print(*aliq(20)) 