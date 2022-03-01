import pandas as pd
import numpy as np

#inicio=int(input('Ingrese año inicial: '))
#final=int(input('Ingrese año final: '))
#ventas = {}
#for i in range(inicio, final+1):
 #   ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': ')) #xreeando dicionario y asignandole valores al diccionario
    
#print(ventas)

#s=pd.Series(ventas)
#print('VENTAS SIN DESCUENTO\n', s)
#print('VENTAS CON DESCUENTO\n', s*0.9) #solo le aplica a los valores


print('-------------2 con Alf------------------')

Cantidad_estudiantes=int(input('cantidad de estudiantes a evaluar: '))

Nombres=[]
Notas=[]
for i in range(Cantidad_estudiantes):
    Nombres.append(input('Nombre alumno: '))
    Notas.append(float(input('Notas alumno: ')))
    
Notas_Alumnos={Nombres:Notas for (Nombres, Notas) in zip(Nombres, Notas)}

print('---------------------------')

S_Notas=pd.Series(Notas_Alumnos)
S_estadisticas=pd.Series([S_Notas.min(), S_Notas.max(), S_Notas.mean(), S_Notas.std()], index=['Minimo', 'Maximo', 'Media', 'Desviación'])
print(S_estadisticas)