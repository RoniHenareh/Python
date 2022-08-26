
# Andra uppgiften: Bygg träd och skriv ut dubbletter

from bintreeFile import Bintree 

svenska = Bintree()

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:

    for rad in svenskfil:
        
        ordet = rad.strip() 

        if ordet in svenska:
            print(ordet, end = " ") # skriver ut dubletter
        else:
            svenska.put(ordet) # in i sökträdet

print("\n")