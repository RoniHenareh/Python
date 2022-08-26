
## syntax

import sys
from linkedQFile import LinkedQ

class FelSyntax(Exception): # subklass
    pass

def read_molekyl(q):

    read_atom(q)

    if q.peek() == '.' or q.peek() == '\n': # kollar om slut
        return
    else:
        read_num(q)
        

def read_atom(q): 

    read_LETTER(q)

    if q.peek() == '.' or q.peek() == '\n': # kollar om slut
        return 
    else:
        read_letter(q)

def empty_queue(q): # tommer listan, för att klara Kattis 

    s = ''

    while q.peek() != '.':
        s += q.dequeue()
    return s

def read_LETTER(q): # syntaxregel
    
    LETTER = q.dequeue() # alltid stor bokstav
    
    sträng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if LETTER not in sträng: 
        raise FelSyntax('Saknad stor bokstav vid radslutet ' + LETTER + empty_queue(q))

def read_letter(q): # syntaxregel
    
    letter = q.peek() # kollar vad det är
    #if letter == None or letter == '.': # Avslutar
        #return

    sträng = 'abcdefghijklmnopqrstuvwxyz'

    if letter in sträng:
        q.dequeue()
    else:
        read_num(q) # eftersom det kan vara stor bokstav och siffra
    return

def read_num(q): # syntaxregel
    
    num = q.dequeue()

    while q.peek() != None and q.peek() != '.':
        num += q.dequeue() # så det kan vara 123 osv.

    if num == None or num == '.': # om inte siffra
        return

    siffervärde = None

    try:
        siffervärde = int(num)
        
    except:
        pass

    if siffervärde == None or siffervärde < 2 or num[0] == '0':
        raise FelSyntax('För litet tal vid radslutet ' + num[1:])


def store(hela): # börjar här

    q = LinkedQ()

    for delen in hela:
        #print('delen', delen)
        q.enqueue(str(delen))

    q.enqueue('.') # markerar slut

    
    return q
    
def testar(hela):

    x = store(hela)

    try: 
        read_molekyl(x)
        return 'Formeln är syntaktiskt korrekt'

    except FelSyntax as fel:
        return str(fel).rstrip('\n')
    
def main():

    for line in sys.stdin.readlines():
        if '#' in line:
            break

        print(testar(line))

if __name__ == '__main__':
    main()
