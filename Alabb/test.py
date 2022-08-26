def hashfunktion(namn):
   summa = 0
   for tkn in namn:
      summa = summa*365 + ord(tkn)
   return summa % 7 + 1

print(hashfunktion('ronih'))