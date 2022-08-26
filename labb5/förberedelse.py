
# förberedelse 

def utskrift(lista):

    if len(lista) > 0:

        print(lista[0])

        utskrift(lista[1:]) # stegar och rekursiv, ger 1, 2, 3, 4, 5

lista = [1,2,3,4,5]
utskrift(lista)

# rita stack frames

def utskrift(lista):

    if len(lista) > 0:

        utskrift(lista[1:]) # stegar så länge len(lista) > 0, sen printar den

        print(lista[0]) # ger 5, 4, 3, 2, 1

lista = [1,2,3,4,5]
utskrift(lista)

# rita stack frames