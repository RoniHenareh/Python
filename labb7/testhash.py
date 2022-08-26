
from pokemon import Pokemon, read_file

from hashFile import Hashtable
from dicthashFile import DictHash   

pokemons = read_file()
n = len(pokemons)

dichash = DictHash()
#dichash = Hashtable(n)

for pokemon in pokemons:

    dichash.store(pokemon.name, pokemon) 


# Pythons dict

dichash.__getitem__('Pikachu') 
dichash.__getitem__('Pikka') 

print(dichash.__contains__('Pikachu'))
print(dichash.__contains__('Pikka'))

# egen hashtabell
'''
print(dichash.search('Pikachu'))
print(dichash.search('Pikka'))'''


