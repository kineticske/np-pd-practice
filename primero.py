import numpy as np
#Cree un objeto ndarray unidimensional con una longitud de 10 y todos 0, y luego haga que el quinto elemento sea igual a 1.
array_zeros=np.zeros((1,10), dtype=int)
array_zeros[0][4]=1
#print(array_zeros)


#2, Crea un objeto ndarray con elementos del 10 al 49.
array_range=np.arange(10,50)
#print(array_range)

#3, Cree una matriz bidimensional de 4 * 4 y genere el tipo de elemento de matriz.
array_4x4z=np.zeros((4,4))
array_4x4i=np.identity(4, dtype=int)
#print(array_4x4z)
#print(array_4x4i)

#print(array_4x4i.dtype.name)

#4, Crea una matriz, que puede completar la transposición de 
#la posición de las coordenadas de (0,1,3) a (3,0,1)
array_t=np.arange(64).reshape(4,4,4) #cant, filas, columnas
#print(array_t)

print('----------------------------')
print('-----------------------------')
array_tt=array_t.transpose(2,0,1)
#print(array_tt)

#5 Convierta el tipo de datos en las 4 preguntas a float64.
print(array_t.dtype.name)
array_t.dtype='float32'
print(array_t.dtype.name)

#6 Utilice el índice booleano para generar los resultados de Rose
s_name=np.array(['tom', 'lilly', 'jack', 'rose'])
s_score=np.array([[79,88,80],[89,90,92], [83,78,85], [78,76,30]])

print(s_score[s_name=='rose'])