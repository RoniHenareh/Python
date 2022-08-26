
# Graf klass 
 
class Vertex: # node/hörn

    def __init__(self, data, parent = None):

        self.data = data # håller koll på nodens/hörnets värde
        self.parent = parent # håller koll på vilka varje nod/hörn är förälder till

        self.connectedTo = dict() # håller koll på vilka noder/hörn varje nod/hörn är barn till
        
    def addRelations(self, i, weight = 0): # lägger till en koppling från denna nod till en annan
        self.connectedTo[i] = weight # kan utökas med vikter

    def __str__(self):
        return str(self.data) + 'connectedTo' + str([x.data for x in self.connectedTo])

    def getConnections(self): # retunerar alla barn till ett ord
        return self.connectedTo.keys() # nycklar

    def getData(self):
        return self.data

    def writechain(self):
        if self.parent != None:
            self.parent.writechain()
        print(self.data)

    def __lt__(self, other):
        return self.data < other.data


class Graph:

    def __init__(self):

        self.vertex = dict() # håller koll på alla noder/hörn

    def addVertex(self, vert): # lägger till node/hörn till grafen
        
        newVertex = Vertex(vert) # vertex objekt
        self.vertex[vert] = newVertex # in i dic ovan

        return newVertex

    def addEdge(self, fromVert, toVert): # lägger till kanter mellan två noder/hörn

        # om inte med i listan
        if fromVert not in self.vertex:
            newVertex = self.addVertex(fromVert)

        if toVert not in self.vertex:
            newVertex = self.addVertex(toVert)

        # kopplar noderna/hörnen om i self.connectedTo
        else:
            self.vertex[fromVert].addRelations(self.vertex[toVert])
            self.vertex[toVert].addRelations(self.vertex[fromVert])

    def __iter__(self): # gör det enklet att iterera över vertex objekten
        return iter(self.vertex.values())









    




