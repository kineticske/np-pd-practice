import numpy as np
#Cree un objeto ndarray unidimensional con una longitud de 10 y todos 0, y luego haga que el quinto elemento sea igual a 1.
array_zeros=np.zeros((1,10), dtype=int)
array_zeros[0][4]=1
print(array_zeros)
