from array import array 

b = array('i')
print(b)

b.append(1)
b.append(2)
b.append(3)
print(b) # [1, 2, 3]

b.pop(0)
print(b)


