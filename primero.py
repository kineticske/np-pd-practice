import numpy as np
#Cree un objeto ndarray unidimensional con una longitud de 10 y todos 0, y luego haga que el quinto elemento sea igual a 1.
array_zeros=np.zeros((1,10), dtype=int)
array_zeros[0][4]=1
print(array_zeros)


#2, Crea un objeto ndarray con elementos del 10 al 49.
array_range=np.arange(10,50)
print(array_range)

#3, Cree una matriz bidimensional de 4 * 4 y genere el tipo de elemento de matriz.
array_4x4z=np.zeros((4,4))
array_4x4i=np.identity(4, dtype=int)
print(array_4x4z)
print(array_4x4i)

print(array_4x4i.dtype.name)
