 
# Trollkarlsprogrammet, sorteringsalgo

ordning = input('Ange vilken ordning ligger korten i: ').split()  #3   1   4   2   5
n = len(ordning)

for i in range(n-1):

    index = i

    for j in range(i+1, n):

        if ordning[index] > ordning[j]:

            index = j


    tmp = ordning[index] 
    ordning[index] = ordning[i] 
    ordning[i] = tmp 

print(ordning) #['1', '2', '3', '4', '5']


