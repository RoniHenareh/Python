# labb 2

from array import array 

# Alla attribut ska vara privata dvs. (inledas med understrykningstecken _).

class ArrayQ: 

    def __init__(self):
        self._first = array('i')

    def enqueue(self, x):
        self._first.append(x)

    def isEmpty(self):
        if len(self._first) == 0:
            return True
        else:
            return False

    def dequeue(self):
        return self._first.pop(0)

    

