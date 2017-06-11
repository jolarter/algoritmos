class HashTable:
    def __init__(self,n):
        self.n = n
        self.arr = [-1 for i in range(0,n)]

    def insertar(self, key, value):
        self.arr[self.hash(key)]=value

    def buscar(self, key):
        return self.arr[self.hash(key)]

    def hash(self, cadena):
        sum = 0
        for i in range(len(cadena)): sum += ord(cadena[i])
        return sum % self.n

    def hash2(self, cadena):
        sum = 0
        for i in range(len(cadena)): sum += ord(cadena[i])*(self.n**i)
        return (sum/self.n) % self.n

    def __str__(self):
        return str(self.arr)

ht = HashTable(17)
ht.insertar("key1","Julian")
ht.insertar("key2","tttt")
ht.insertar("key3","Laura")
print(ht)
print(ht.buscar("key1"))
print(ht.buscar("key2"))
print(ht.buscar("key3"))
