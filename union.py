
class UnionFindwPathC:
    def __init__(self,n):
        self.arr = [-1 for i in range(0,n)]

    def union(self,dat1,dat2):
        root1,root2 = self.find(dat1),self.find(dat2)
        if self.arr[root1] <= self.arr[root2]:
            self.arr[root2] = root1
        else:
            self.arr[root1] = root2

    def comp(self,dat1,dat2):
        root1,root2 = self.find2(dat1),self.find2(dat2)
        return True if (dat1 == dat2 or root1 == root2) and self.arr[root1]+self.arr[root2]<0 else False

    def __str__(self):
        return str(self.arr)

    """ find sin acortar camino """
    def find(self, dat):
        return dat if self.arr[dat] < 0 else self.find(self.arr[dat])

    """ find CON acortar camino """
    def find2(self, dat):
        if self.arr[dat] < 0:
            r = dat
        else:
            r = self.arr[dat] = self.find(self.arr[dat])
        return r

tam = 20
conjunto = UnionFindwPathC(tam)
print("{5,6,7,8} {10,11,12,13,0,1,2,3} {9} {14} {15} {16} {17} {18} {19} ...")
conjunto.union(5,6)
conjunto.union(6,7)
conjunto.union(7,8)
conjunto.union(10,11)
conjunto.union(11,12)
conjunto.union(11,13)
conjunto.union(0,1)
conjunto.union(0,2)
conjunto.union(1,3)
conjunto.union(0,12)

"""print([-i for i in range(0,tam)])"""
print(conjunto)

print("comp 0 12 "+str(conjunto.comp(0,12)))
print("comp 5 17 "+str(conjunto.comp(5,17)))
print("comp 1 10 "+str(conjunto.comp(1,10)))
print("comp 18 19 "+str(conjunto.comp(18,19)))
print("comp 6 2 "+str(conjunto.comp(6,2)))

print("Se une 0,5")
conjunto.union(0,5)
print(conjunto)

print("comp 6 2 "+str(conjunto.comp(6,2)))
