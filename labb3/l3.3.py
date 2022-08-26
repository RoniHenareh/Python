
# Tredje uppgiften: Två binära sökträd med ordlistor

from bintreeFile import Bintree

svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:

    for rad in svenskfil:

        ordet = rad.strip()                # Ett trebokstavsord per rad

        if not ordet in svenska:
            
            svenska.put(ordet)             # in i sökträdet
        
engelska = Bintree()
with open("engelska.txt", "r", encoding="utf-8") as engfil:

    for rad in engfil:

        for ord in rad.split(): # delar upp på mellanslag
            ordet = ord.strip() # tar bort all skit

            if not ordet in engelska:
                engelska.put(ordet)

                if ordet in svenska:
                    print(ordet, end=' ')
print()