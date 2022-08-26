import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

from hashFile import Hashtable
from passwords import passwd as vanligaLösenord # intressant

listanStorlek = 10000 # konstant
h = Hashtable(listanStorlek)

def count_collisions(generated_hashes):

    sum = 0

    for h in generated_hashes.keys():
        sum += generated_hashes[h] - 1 # annars fler än antalet försök

        '''if generated_hashes[h] > 2:
            print(h)'''

    return sum

def calculate_hashes(hash, size):

    generated_hashes = {}

    #gamla_lösenord = []
    
    for lösenord in vanligaLösenord[:size]:

        '''gamla_lösenord.append(lösenord)
        if lösenord == gamla_lösenord:
            print(f'upprepning av {lösenord}')'''
            
        hashvärde = hash(lösenord)

        '''if size == 100:
            print(hashvärde)'''

        if hashvärde in generated_hashes.keys():
            #print(lösenord)
            generated_hashes[hashvärde] += 1

        else: 
            generated_hashes[hashvärde] = 1

    return generated_hashes


def test(hash):

    data = []

    size = 10000
    generated_hashes = calculate_hashes(hash, size)
    sum = count_collisions(generated_hashes)
    data.append((size, sum))

    size = 1000
    generated_hashes = calculate_hashes(hash, size)
    sum = count_collisions(generated_hashes)
    data.append((size, sum))

    size = 100
    generated_hashes = calculate_hashes(hash, size)
    sum = count_collisions(generated_hashes)
    data.append((size, sum))

    return data

def main():

    hash = h.hashfunction

    data_egen_hash = test(hash)

    #print(data_egen_hash)

    data1 = data_egen_hash.pop(0)
    data2 = data_egen_hash.pop(0)
    data3 = data_egen_hash.pop(0)

    '''print(data1)
    print(data2)
    print(data3)'''

    # tuples
    listanStorlek1, antalKollisioner1 = data1
    listanStorlek2, antalKollisioner2 = data2
    listanStorlek3, antalKollisioner3 = data3
    
   # plotta

    plt.figure(figsize=(8,5))
    plt.grid()
    plt.xlabel('Listans storlek')
    plt.ylabel('Antal kollisioner')

    plt.plot([listanStorlek1], [antalKollisioner1], 'ro', label = '10000')
    plt.plot([listanStorlek2], [antalKollisioner2], 'bo', label = '1000')
    plt.plot([listanStorlek3], [antalKollisioner3], 'ko', label = '100')

    plt.legend(loc = 'upper left')
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()

