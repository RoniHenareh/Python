
# Skapa en ArrayQ-modul

from arrayQFile import ArrayQ 
# Nu går det att använda klassen utan att den syns i programmet


if __name__ == "__main__": # så det inte blir jidder vid import

    q = ArrayQ()

    q.enqueue(3)
    q.enqueue(4)

    x = q.dequeue()
    y = q.dequeue()

if (x == 3 and y == 4):
    print("OK")
else:
    print("FAILED")