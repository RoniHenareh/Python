# klass som representerar en Pokemon

class Pokemon: 

    def __init__(self, name, type1, type2, total, hp, attack, defense, spatk, spdef, speed, generation, legendary):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.spatk = spatk
        self.spdef = spdef
        self.speed = speed
        self.generation = generation
        self.legendary = legendary

    def __str__(self):
        return self.name + ' ' + self.type1 + ' ' + self.type2 + ' ' + self.total + ' ' + self.hp + ' ' + self.attack + ' ' + self.defense + ' ' + self.spatk + ' ' + self.spdef + ' ' + self.speed + ' ' + self.generation + ' ' + self.legendary

    def __lt__(self, other):
        return self.total < other.total 

    def __gt__(self,other):
        return self.total > other.total 


def main():

    f = open('data.csv', 'r', encoding = 'UTF-8')
    lista = f.read() # read ty readlines skapar lista
    f.close

    info_rader = lista.split('\n') # notera split funkar ej på lista
    #print(info_rader)

    pokemons = list()

    for rad in info_rader:

        info = rad.split(',')
        pokemons.append(Pokemon(info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9], info[10], info[11],  info[12]))

    for pokemon in pokemons:

        # ty dem vill att vi använder __str__
        print(pokemon.name, pokemon.type1, pokemon.type2, pokemon.total, pokemon.hp, pokemon.attack, pokemon.defense, pokemon.spatk, pokemon.spdef, pokemon.speed, pokemon.generation, pokemon.legendary) 
        #pass
    search(pokemons)

def search(pokemons):
    
    fråga = input('Ange en pokemon som du vill få mer information om: ')

    for pokemon in pokemons:
        if pokemon.name == fråga:
            print(pokemon)

main()

# testar lt och gt

#test1 = Pokemon('Trevenant', 'Ghost', 'Grass', '474', '85', '110', '76', '65', '82', '56', '6', 'False')
#test2 = Pokemon('Trevenant', 'Ghost', 'Grass', '500', '85', '110', '76', '65', '82', '56', '6', 'False') 

'''print(test1 > test2)
print(test2 > test1)

print(test1 < test2)
print(test2 < test1)'''