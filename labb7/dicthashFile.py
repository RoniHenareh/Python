
# egen hashtabell med Pythons dictionary

class DictHash:   

    def __init__(self):

        self.dic = dict()

    def __getitem__(self, nyckel):
        # retunerar nyckelns värde
        return search(self, nyckel) 

    def __contains__(self, nyckel):
        # testar om nyckel är med i listan
        if nyckel in self.dic: # inte: nyckel in self.dic[nyckel]
            return True
        else:
            return False

    def store(self, nyckel, data):
        # utökar dic med nycklar och värden
        self.dic[nyckel] = data


def search(self, nyckel):
    
    try:
        if nyckel in self.dic:
            print(self.dic[nyckel])
        else:
            raise KeyError(f'{nyckel} är inte med i listan')

    except KeyError as s:
        print(s)

   

    
