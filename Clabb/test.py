
import matplotlib.pyplot as plt
from hashFile import Hashtable
import hashlib
import random
import zlib

def sha512(b):
    hs = hashlib.sha512(b).hexdigest()
    return int(hs, 16)

def adler32(key): 

    # Adler-32
    # using zlib.adler32() method
    värde = zlib.adler32(bytes(str(key), 'UTF-8'))
    
    return värde 

# skapar strängar
def create_string(l):
    s = ""
    for _ in range(l):
        s += chr(random.randint(28, 127))
        #print('string', s)
    return s

# flippar bitar
def flip_bit(bits, pos):

    pos += 2
    bit = bits[pos]

    if bit == '0':
        bit = '1'

    else:
        bit = '0'

    new_bits = bits[:pos] + bit + bits[pos+1:]

    return bin(int(new_bits, 2))

# beräknar antalet olika bitar för två hashvärden
def diff_bits(h1, h2):

    h1 = pad(h1, len(h2))
    h2 = pad(h2, len(h1))
    n = 0

    for i in range(len(h1)):
        if h1[i] != h2[i]:
            n += 1
    return n

# padding
def pad(bits, length):
    return format(int(str(bits), 2), f'0{length}b')

# beräknar antal bitar från binär form
def number_of_bits(bits):
    return len(bits) - 2

def testaFöränndring(hash_func, string_length, deviations):

    original_string = create_string(string_length) # skapar strängar med olika storlek
    original_bytes = bytes(original_string, 'UTF-8') # gör om till bytes
    original_bits = bin(int.from_bytes(original_bytes, byteorder='big')) # skriver på binär form ?
    original_hash = bin(hash_func(original_bytes)) # hashar bytes och skriver på binär form ?
    
    for i in range(number_of_bits(original_bits)):

        new_bytes = original_bytes
        new_bits = bin(int.from_bytes(new_bytes, byteorder='big'))

        flipped_bits = flip_bit(new_bits, i)
        flipped_bytes = int(flipped_bits, 2).to_bytes(len(new_bytes), byteorder='big')

        new_hash = bin(hash_func(flipped_bytes))

        # beräknar skillnaden i bitar från två hashvärden och dividerar men antalet bitar
        # dett ger oss andelen som förändras, sedan stoppar vi in det i vår lista
        deviations.append(abs(diff_bits(original_hash, new_hash)) / number_of_bits(original_hash))

    return deviations

# skapar olika längder på strängarna som testas
def test_hash(hash_func):
    
    deviations = []

    for l in range(1, 19): # för varje l
        testaFöränndring(hash_func, l, deviations)

    return deviations
    

def main():

    repeats = 500 
    number_of_bins = 50 # printar

    h = Hashtable(repeats)
    hash_func = h.hashfunction

    adler_deviations = test_hash(adler32) # testar förändring
    print('Värden för Adler32:', end = ' ')
    print('Andelen', sum(adler_deviations) / len(adler_deviations), end = ', ')
    print('längden', len(adler_deviations))

    hash_deviations = test_hash(hash_func) # testar förändring

    for num in hash_deviations:
        if num > 1:
            hash_deviations.remove(num)

    print('Värden för egen hash:', end = ' ')
    print('Andelen', sum(hash_deviations) / len(hash_deviations), end = ', ')
    print('längden', len(hash_deviations))

    sha512_deviations = test_hash(sha512)
    print('Värden för sha512:', end = ' ')
    print('Andelen', sum(sha512_deviations ) / len(sha512_deviations ), end = ', ')
    print('längden', len(sha512_deviations ))

    # printar
    plt.hist(adler_deviations, number_of_bins, density = True, facecolor = 'g', label = 'Adler32')
    plt.hist(hash_deviations, number_of_bins, density = True, facecolor = 'r', label = 'Egen hash')
    plt.hist(sha512_deviations , number_of_bins, density=True, facecolor='b', alpha=0.75, label="SHA512")
    plt.legend()
    plt.xlabel('Andel flippade bitar')
    plt.ylabel('Andel utfall (%)')
    plt.title('Avalanche effect')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()