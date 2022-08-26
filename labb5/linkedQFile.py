
# LinkedQ - en kö av noder (länkad lista)

class Node:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        

class LinkedQ:

    def __init__(self): # startvärden 
       self.first = None
       self.last = None

    def enqueue(self, data):

        tmp = Node(data) # nya värdet

        if self.first == None: 
            self.first = tmp
            self.last = self.first

        else: 
            self.last.next = tmp # pekar på nya värdet
            self.last = tmp # sätter in nya värdet längst bak

    def dequeue(self):

        tmp = self.first # första värdet i kön
        self.first = self.first.next # pekar på andra platsen i kön

        return tmp.data

    def isEmpty(self):

        if self.first == None: # tom
            return True
        else:
            return False
        




