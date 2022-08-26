
from readFile import Music, read_file
import timeit

def main():

    lista = read_file()

    # för att slice:a
    
    #testlista = read_file()

    #lista = testlista[0:250000]
    #lista = testlista[0:500000]

    #lista = testlista[0:1000]
    #lista = testlista[0:10000]
    #lista = testlista[0:100000]
    #lista = testlista[0:1000000]
    
    n = len(lista)
    print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista.artistnamn

    # sorterar för binärsökning
    sorterad_lista = sorted(lista) #attrgetter('artistnamn')), behöves ej ty lt/gt

    # sorterar  listan för hash
    artister = dict()

    # först allt in i en dic
    for music in lista:

        if music.artistnamn in artister:
            artister[music.artistnamn].append(music)
        else:
            artister[music.artistnamn] = [music]

    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    bintid = timeit.timeit(stmt = lambda: binsok(sorterad_lista, testartist), number = 10000)
    print("Binärsökning tog", round(bintid, 4) , "sekunder")

    hashtid = timeit.timeit(stmt = lambda: hashsok(artister, testartist), number = 10000)
    print("Hashsökning tog", round(hashtid, 4) , "sekunder")

    # måste köras en i taget, intressant!
    '''bubbletid = timeit.timeit(stmt = lambda: bubblesort(lista), number = 1)
    print("Bubblesort tog", round(bubbletid, 4) , "sekunder")'''

    '''insättid = timeit.timeit(stmt = lambda: insättningssortera(lista), number = 1)
    print("insättningssortering tog", round(insättid, 4) , "sekunder")'''

def linsok(lista, testartist): # kräver osorterad lista

    n = 0
    for i in range(len(lista)):
        n += 1
        if lista[i].artistnamn == testartist:
            #print('Linjärsökning hittade {0} på index {1} på {2} steg'.format(testartist, i, n))
            break

def binsok(sorterad_lista, testartist): # kräver sorterad lista

    n = 0
    start = 0
    end = len(sorterad_lista) - 1

    while (start <= end):

        # stega
        n += 1
        # beräkna mitten
        mid = int((start + end) / 2)
          
    # testa om svaret i mitten
        if sorterad_lista[mid].artistnamn == testartist: 
            #print('Binärsökning hittade {0} på index {1} på {2} steg'.format(testartist, mid, n))
            break

        elif sorterad_lista[mid].artistnamn  < testartist: # större
            start = mid + 1 # fortsätt sökningen på höger sida
            
        elif sorterad_lista[mid].artistnamn  > testartist: # mindre
            end = mid - 1 # fortsätt sökningen på vänster sida

def hashsok(artister, artist):
    #hitta det vi söker
    return artister[artist]

# sorteringsalgoritmer från föreläsning 9

def bubblesort(data): 

    n = len(data)
    fortsätt = True
    i = 0

    while fortsätt:
        fortsätt = False

        for j in range(n-1-i):
            if data[j+1].artistnamn < data[j].artistnamn: # jmf
                data[j+1].artistnamn, data[j].artistnamn = data[j].artistnamn, data[j+1].artistnamn # byt

            fortsätt = True
            #print(data)

        i += 1

def insättningssortera(data):
    n = len(data)

    for i in range(1, n):

        varde = data[i]
        plats = i

        while plats > 0 and data[plats-1].artistnamn > varde.artistnamn:
            data[plats].artistnamn = data[plats-1].artistnamn
            plats = plats - 1

        data[plats].artistnamn = varde.artistnamn

if __name__ == '__main__':
    main()