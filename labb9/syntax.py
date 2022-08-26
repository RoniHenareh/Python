
## syntax

atoms = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']

import sys
from linkedQFile import LinkedQ

class FelSyntax(Exception): # subklass
    pass

def read_formel(q):
    
    while q.peek() != '.' and q.peek() != '\n':

        read_mol(q)

def read_mol(q):
    
    read_group(q)

def read_group(q):
    
    if q.peek() == '(': 
        read_parantes(q) 
        return

    read_atom(q) # om vanlig atom
 
    if q.peek() == ')': # om bara slutparentes
        raise FelSyntax(f'Felaktig gruppstart vid radslutet {empty_queue(q)}' )

    if q.peek() == '.' or q.peek() == '\n': # kollar om slut
        return
    else:
        read_num(q)

def read_parantes(q): # testar allt med parenteser

    q.dequeue()

    while q.peek() != '.' and q.peek() != '\n' and q.peek() != None:

        read_atom(q)
        read_num(q)

        if q.peek() == '(': # rekusivt
            read_parantes(q) # så kan vara flera parenteser

        if q.peek() == ')':

            q.dequeue()
            
            if not read_num(q): # om inte siffra efter slutparentes
                raise FelSyntax(f'Saknad siffra vid radslutet {empty_queue(q)}')
            return

        # fortsätter att skapa atomer i parenteser
        
    raise FelSyntax(f'Saknad högerparentes vid radslutet') # om ingen slutparentes

def read_atom(q): # syntax reglen LETTER och letter

    big_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_letter = big_letter.lower()

    all_letters = big_letter + small_letter

    atom = ''

    if q.peek() not in all_letters:
        # specialtecken typ parentes
        raise FelSyntax(f'Felaktig gruppstart vid radslutet {empty_queue(q)}' )


    if q.peek() not in big_letter:
        # om startar atom med liten bokstav
        raise FelSyntax(f'Saknad stor bokstav vid radslutet {empty_queue(q)}' )

    else:

        # skapar atomen
        atom = q.dequeue()

        if q.peek() in small_letter:
            atom += q.dequeue()

    if atom not in atoms:
        raise FelSyntax(f'Okänd atom vid radslutet {empty_queue(q)}' )


    if q.peek() == '.' or q.peek() == '\n': # kollar om slut
        return 
        
def empty_queue(q): # tommer listan, för att klara Kattis 

    s = ''

    while q.peek() != '.':
        s += q.dequeue()
    return s

def read_num(q): # syntaxregel

    found_number = False # bool
    
    numbers = '0123456789'
    num = ''

    while q.peek() in numbers:
        num += q.dequeue() # så det kan vara 123 osv.

    if len(num) == 0:
        return found_number  # hittade inte

    if num == '.' or num == '\n': # om inte siffra
        return found_number # hittade inte

    siffervärde = None

    try:
        siffervärde = int(num)
        found_number = True # hittade
    except:
        pass

    if siffervärde == None or siffervärde < 2 or num[0] == '0':
        raise FelSyntax(f'För litet tal vid radslutet {num[1:]}{empty_queue(q)}')
    return found_number

def store(hela): # börjar här

    q = LinkedQ()

    for delen in hela:
        q.enqueue(str(delen))

    q.enqueue('.') # markerar slut

    
    return q
    
def testar(hela):

    x = store(hela)

    try: 
        read_formel(x)
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
