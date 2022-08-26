
import math
import zlib
 
class Node:  

    def __init__(self, key, data, next = None): 
        self.key = key
        self.data = data

        self.next = next
    
    def find_next(self, nod):
        # krockhantering
       
        # samma nyckel skriver över
        if self.key == nod.key:
            self.data = nod.data

        # lägger till om tom plats
        elif self.next == None:
            self.next = nod
        else:
            self.next.find_next(nod)

    def find_key(self, key):
        # hittar rätt nyckel

        # går igenom kedjan
        if self.key == key:
            return self.data
        else:
            if self.next != None:
                return self.next.find_key(key)
            else:
                raise KeyError

class Hashtable:

    def __init__(self, size):

        # startvärden 
        self.first = None
        self.last = None

        # skapar 50 % luft
        self.size = size * 2
        self.lista = [None] * self.size
 
    def store(self, key, data):

        keyHash = self.hashfunction(key) 
        nod = Node(key, data)

        # krockhantering

        if self.lista[keyHash] == None:
            self.lista[keyHash] = nod
           
        elif self.lista[keyHash] != None:
            self.lista[keyHash].find_next(nod) 

    def search(self, key):  

        keyHash = self.hashfunction(key)

        # hittar rätt nyckel

        if self.lista[keyHash] == None:
            raise KeyError('nyckeln är inte med i listan')
        else:
            return self.lista[keyHash].find_key(key)


    '''def hashfunction(self, key): # utvidga

        # form av mid square

        #print(f'nyckeln är: {key}')
        key_värde = 0

        n = len(str(self.size))

        for k in key:
            key_värde += ord(k)
        #print(f'summan av alla ord i nyckeln blir {key_värde}')

        kvadera = str(math.pow(key_värde, 2))
        lista = list(kvadera)
        #print(f'nyckeln kvadrerat i en lista blir {lista}')

        nytt = (str(lista[0]) + str(lista[1]) + str(lista[2])) * n
        #print(f'nyckeln {key} blir tillslut till {nytt}')

        nytt_värde = hash(nytt)

        return nytt_värde % self.size'''

    
    def hashfunction(self, key): 

        # Adler-32
        # using zlib.adler32() method
        värde = zlib.adler32(bytes(str(key), 'UTF-8'))
    
        return värde % self.size


# test för c labben
#nr = 980203 % 7 + 1
#print(nr) ger 1
