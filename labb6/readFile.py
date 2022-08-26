
# klass som representerar låtar
# trackid<SEP>låtid<SEP>artistnamn<SEP>låttitel

class Music: 

    def __init__(self, trackid, låtid, artistnamn, låttitel):
        
        self.trackid = trackid
        self.låtid = låtid
        self.artistnamn = artistnamn
        self.låttitel = låttitel

    '''def __str__(self):
        return self.trackid + ' ' + self.låtid + ' ' + self.artistnamn + ' ' + self.låttitel'''

    def __lt__(self, other):
        return self.artistnamn < other.artistnamn

    def __gt__(self,other):
        return self.artistnamn > other.artistnamn 

        
def read_file():

    f = open('unique_tracks.txt', 'r', encoding = 'UTF-8')
    lista = f.read() # read ty readlines skapar lista
    f.close

    info_rader = lista.split('\n') # notera split funkar ej på lista
    #print(info_rader)

    musiken = list()

    for rad in info_rader:

        info = rad.split('<SEP>')
        #print('info', info)

        #print('_str_', Music(info[0], info[1], info[2], info[3]))
        musiken.append(Music(info[0], info[1], info[2], info[3]))
        
    #print('musiken', musiken) # lista med musikobjekt

    '''for musik in musiken:

        print(musik.trackid, musik.låtid, musik.artistnamn, musik.låttitel)'''

    return musiken



    
