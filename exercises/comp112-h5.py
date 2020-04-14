bagCap = int(input("Bag capacity: "))
items = int(input("Items : "))
v = list()
w = list()
m = list()
print(max(5,6))
for i in range(items):
    m.append([0])
    for j in range(1, bagCap):
        m[i].append(0)

print("For items weights and values")
for i in range(items):
    w.append(int(input("{}.Weight: ".format(i))))
    v.append(int(input("{}.Value: ".format(i))))

for i in range(items):
    for j in range(bagCap):
        if w[i] > j:
            m[i][j] = m[i-1][j]
        else:
            m[i][j] = max(m[i-1,j], m[i-1, j-w[i]]+v[i])
            
