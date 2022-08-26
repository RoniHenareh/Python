
# kortaste vägen till en bokstav 
# söt -> söm -> döm -> dum -> dur -> sur
# alla mellanliggande ord måste ligga i ordlistan  

from graphFile import Graph
from linkedQFile import LinkedQ
from bintreeFile import Bintree

def main():

    dic = dict()
    graf = Graph()

    with open("word3.txt", "r", encoding = "utf-8") as ordlista:

        for ord in ordlista:
            word = ord.strip()

            # skapar buckets som diffar bokstav
            for i in range(len(word)):
                bucket = word[:i] + ' ' + word[i+1:] 

                if bucket in dic: 
                    dic[bucket].append(word) 
                else:
                    dic[bucket] = [word] 
                    
    # lägger till hörn och kanter till ord i samma bucket
    for bucket in dic.keys():
        
        for word1 in dic[bucket]:
            for word2 in dic[bucket]:
                if word1 != word2:
                    graf.addEdge(word1, word2) 

    '''for v in graf.vertex['söt'].getConnections():
        print(v.data) # alla barn till söt'''

    #print(q.isEmpty())

    startord = input('Startord: ')
    slutord = input('Slutord: ')

    makechildren(startord, slutord, graf)

    #print(q.isEmpty())

    return graf


def makechildren(startord, slutord, graf):

    gamla = Bintree()
    lista = LinkedQ()

    gamla.put(graf.vertex[startord]) # BFS

    for child in graf.vertex[startord].getConnections(): # för varje barn till startordet

        child.parent = graf.vertex[startord] # definerar förälder till sina barn

        lista.enqueue(child) # som nu ligger i listan
        gamla.put(child)

    # hitta nu barnens barn, rekursivt
    while not lista.isEmpty():

        nod = lista.dequeue()

        for child in graf.vertex[nod.data].getConnections(): # för varje nod/hörn

            if child not in gamla:
                
                child.parent = nod

                lista.enqueue(child) # som nu ligger i listan
                gamla.put(child)

        if nod.data == slutord:
            nod.writechain()
            break

        if lista.isEmpty() == True:
            print('Det finns ingen väg!')
    
if __name__ == '__main__':
    main()
   


       







