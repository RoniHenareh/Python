
f = open("word3.txt", "r", encoding = "utf-8")
lista = f.readlines()
f.close

for rad in lista:
    ordet = rad.strip(' ')  

    print(ordet)