from numpy import linspace
from marbles import *
from matplotlib import pyplot as plt
from timeit import default_timer as timer

def test_main():

    for i in ['1', '2', '3']:

        fortsätt = True
        startTid = timer()

        tid_lista = list()
        N_lista = list()

        with open(f'fall{i}.txt', encoding= 'UTF-8') as file:

            antalFall_tot = 0 # börjar om för varje fall
            
            while fortsätt:

                antalFall = file.readline() # 9

                lista = list()

                if int(antalFall) == 0:

                    fortsätt = False
                    continue # tillbaka till while

                for j in range(int(antalFall)):
                    fall = file.readline()
                    information = list(map(int, (fall.split())))
                    lista.append(information)
                    #print('information', information)

                svar = readdata(antalFall, lista)

                antalFall_tot += int(antalFall)
                #print(f'index{i} har totalt antal fall {antalFall_tot}')

                
                slutTid = timer()
                tid_lista.append(slutTid)
                N_lista.append(antalFall_tot)

                
        #print(tid_lista)
        #print(N_lista)

    x = linspace(0, 450, 2)
    #y = 0.00000333*x + 0.415
    k = (tid_lista[-1] - tid_lista[0]) / (N_lista[-1] - N_lista[0])
    y = tid_lista[0] + k*x
    plt.figure(figsize=(8, 6))
    plt.plot(N_lista, tid_lista, 'g', label = 'från data')
    plt.plot(x, y, 'r', label = 'rät linje')
    plt.xlabel('Antal fall N')
    plt.ylabel('Tid t')
    plt.legend()
    plt.show()





test_main()