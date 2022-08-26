# labb 2

from array import array 

# Alla attribut ska vara privata dvs. (inledas med understrykningstecken _).

class ArrayQ:

    def __init__(self):
        self.first = array('i')

    def enqueue(self, x):
        self.first.append(x)

    def dequeue(self):
        return self.first.pop(0)

q = ArrayQ()
q.enqueue(1)
q.enqueue(2)

x = q.dequeue()
y = q.dequeue()

if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")

