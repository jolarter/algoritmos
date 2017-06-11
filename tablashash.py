class HashTable:
    def __init__(self,n):
        self.arr = [-1 for i in range(0,n)]
    def insertar(self, key, value):
        pass
    def buscar(self, key):
        pass
    def hash(cadena, tam):
        sum = 0
        for pos in range(len(cadena)):
            sum += ord(cadena[pos])
        return sum%tam
