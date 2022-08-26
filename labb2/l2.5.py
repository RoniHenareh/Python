
# Trollkarlsprogrammet med LinkedQ/ArrayQ

from arrayQFile import ArrayQ 
#from linkedQFile import LinkedQ

if __name__ == "__main__":

    q = ArrayQ()                                             
    #q = LinkedQ()

    ordning = input('Ange vilken ordning ligger korten i: ').split()  # 3   1   4   2   5
    n = len(ordning)

    for i in range(n):

        q.enqueue(int(ordning[i])) # Siffrorna läggs i samma ordning som dem angavs i
        # ['3', '1', '4', '2', '5']
   
    nyordning = []

    while q.isEmpty() == False:

        x = q.dequeue() # plockar ut första värdet i listan
        q.enqueue(x) # skickar samma värde sist i listan
        # [3   1   4   2   5]
        # [1   4   2   5   3]
      
        nyordning.append(q.dequeue()) # Skickar nu värdet med index 0 till den nya listan
        # [1]
        # [4   2   5   3]
        # osv.
        
        

    print('De kommer ut i denna ordning:', nyordning)     

    