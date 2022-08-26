
# kortaste vägen till en bokstav 
# söt -> söm -> döm -> dum -> dur -> sur
# alla mellanliggande ord måste ligga i ordlistan
# programmet ska bara avgöra om det är möjligt eller ej

from bintreeFile import Bintree
from linkedQFile import LinkedQ

def main():
    
    bintree = Bintree()

    with open("word3.txt", "r", encoding = "utf-8") as ordfil:

        for rad in ordfil:

            ordet = rad.strip() # Ett trebokstavsord per rad 

            if ordet in bintree:
                pass # hoppar dubletter
            else:
                bintree.put(ordet) # annars in i sökträdet

    startord = input('Startord: ')
    slutord = input('Slutord: ')

    #makechildren1(startord, bintree)
    makechildren2(startord, slutord, bintree)
    

# första versionen, hitta alla barn till ett startord
def makechildren1(startord, bintree):

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
    ord = list(startord) # intressant!

    orden = list() # barnen

    # hittar alla möjliga kombinationer till startordet
    for i in range(len(ord)):
        ord = list(startord)
        for j in range(len(letters)):

            ord[i] = letters[j]
            ord_ihop = ''.join(ord) # intressant!

            if bintree.__contains__(ord_ihop) == True and ord_ihop != startord:
                #print(ord_ihop) # om kombinationen är ett riktigt ord printar vi det
                orden.append(ord_ihop) # och lägger in barnen i listan orden 

    return orden 


# andra versionen, avgör om det finns en väg

def makechildren2(startord, slutord, bintree):

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']

    ord = list(startord)

    gamla = Bintree()
    q = LinkedQ()
    
    q.enqueue(startord) # 1. breddenförstsökning

    # hittar alla möjliga kombinationer till startordet
    for i in range(len(ord)):
        ord = list(startord)
        for j in range(len(letters)):

            ord[i] = letters[j]
            ord_ihop = ''.join(ord)

            if ord_ihop == slutord:
                print('Det finns en väg till', slutord)
                break

            # om kombinationen är ett riktigt ord stoppar vi in det i kön
            if bintree.__contains__(ord_ihop) == True and ord_ihop != startord:
                gamla.put(ord_ihop) # gamla håller koll på dubletter
                q.enqueue(ord_ihop) # används för att skapa flera barn

            else:
                continue 
        
    # 2. breddenförstsökning
    while not q.isEmpty():

        nod = q.dequeue()
        children = makechildren1(nod, bintree) # ger alla barnens barn

        for child in children:
            if child not in gamla:
                # lägger till alla barn i kön
                q.enqueue(child) # om det inte finns i gamla
                gamla.put(child) # samt uppdaterar gamla

        if nod == slutord:
            print('Det finns en väg till', slutord)
            break

        if q.isEmpty() == True:
            print('Det finns ingen väg!')
           
if __name__ == '__main__':
    main()
   


       







