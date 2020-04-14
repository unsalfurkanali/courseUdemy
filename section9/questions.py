from functions import reduce
def area(tup):
    return tup[0]*tup[1] 

def triangular(tup):
    a, b, c = tup[0], tup[1], tup[2]
    if abs(b-c) < a < b+c and abs(a-b) < c < a+b and abs(a-c) < b < a+c:
        return True
    else:
        return False

square = [(4,5), (8,9), (3,7), (6,8)]
area = list(map(area, square))
print("Areas", *area)
triang = list(filter(triangular, [(3,4,5), (6,8,10), (3,9,7)]))
print("Triangular", *triang, sep=", ")
sumList = [1,2,3,4,5,6,7,8,9,10]
total = reduce(lambda x,y: x+y ,list(filter(lambda x: x%2 == 0, sumList)))
print("Total ", total)
names = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
lastName = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
for i,j in zip(names, lastName):
    print(i,j)