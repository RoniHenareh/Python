
## A Labben

class Node:

    def __init__(self, vertexIndex, numMarbles, numChildren, childrenIndex):

        # väljs
        self.vertexIndex = vertexIndex # varje vertex har ett nummer
        self.numMarbles = numMarbles # antal kulor hos varje vertex
        self.numChildren = numChildren # antal barn för varje vertex
        self.childrenIndex = childrenIndex # varje barn har ett nummer

        # för alla
        self.parent = None
        self.need = 0
        
        self.childrenNodes = []
        
    def __repr__(self):
        return str(self.vertexIndex)

    # lägger till alla barn i en lista
    def makeChildren(self, child):
    
        self.childrenNodes.append(child)

        #definerar förälder
        # notera var None först
        child.parent = self

    # beräknar kulor varje barn behöver
    def howManyMarbles(self):
        
        # om 0 så behövs en kula
        # om -x finns det x kulor över
        need = 1 - self.numMarbles 
        
        # rekursivt
        for child in self.childrenNodes:
            #print('test', child.parent)
            need += child.howManyMarbles() 

        # uppdaterat i klassen
        self.need = need

        return need
    
    # beräknar antalet flyttar som krävs
    def howManyMoves(self):

        flyttar = 0

        # rekursivt
        for child in self.childrenNodes:
            flyttar += child.howManyMoves()

        if self.parent != None: # om har en förälder

            self.parent.numMarbles -= self.need # tar kulor från föräldern
            self.numMarbles += self.need # adderar kulor hos barnen

            flyttar += abs(self.need) # antal flyttar
            self.need -= self.need # uppdaterar barnens behov

        return flyttar
       

def readdata(antalFall, allInformation):

    # återställer
    root = None
    nodlista = []
    totFlyttar = 0

    for information in allInformation:

        vertexIndex = information[0] # nummer för varje vertex
        numMarbles = information[1] # antal kulor i den vertexen
        numChildren = information[2] # antal barn till den första vertexen
        childrenIndex = information[3:] # nummer för barn till den första vertexen

        nod = Node(vertexIndex, numMarbles, numChildren, childrenIndex) # skapar nod-objekt
        nodlista.append(nod) # lägger in nod-objekt i nodlistan
        #print('nod', nod)

    for i in range(antalFall): #range(int(antalFall)): #ändrat för kattis
        for j in nodlista[i].childrenIndex: # för alla barn i nodlistan
            nodlista[i].makeChildren(nodlista[j-1]) # lägger vi till barnnen i en egen lista

    for child in nodlista: # kollar om har en förälder
        if child.parent == None: # om inte, är det rooten
            #print('hittar root')
            #print('child', child)
            root = child 
            break

    root.howManyMarbles() # beräknar vi hur många kulor som behövs
    totFlyttar = root.howManyMoves() # beräknar totala antalet flyttar som behövdes

    return totFlyttar

def main():

    fortsätt = True

    while fortsätt:

        antalFall = int(input())

        lista = list()

        if antalFall == 0:

            fortsätt = False
            continue # tillbaka till while

        for i in range(antalFall):
            information = list(map(int, (input().split())))
            lista.append(information)
            #print('information', information)

        #print('information', lista)
        svar = readdata(antalFall, lista)
        print(svar)

if __name__ == '__main__':
    main()

