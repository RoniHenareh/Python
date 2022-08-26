
# LinkedQ - en kö av noder (länkad lista)

class Node:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedQ:

    def __init__(self): 
       self.first = None
       self.last = None

    def enqueue(self, data):

        tmp = Node(data) 

        if self.first == None: 
            self.first = tmp
            self.last = self.first

        else: 
            self.last.next = tmp 
            self.last = tmp 

    def dequeue(self):

        if self.isEmpty(): # om tom
            return None
        else:

            tmp = self.first 
            self.first = self.first.next 

        return tmp.data

    def isEmpty(self):

        if self.first == None: # tom
            return True
        else:
            return False

    def peek(self): # forts, endast för labb 8

        if self.isEmpty(): # om tom
            return None

        else:

            tmp = self.first.data
            
            return tmp







        




