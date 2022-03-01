import pandas as pd
import numpy as np

inicio=int(input('Ingrese año inicial: '))
final=int(input('Ingrese año final: '))
ventas = {}
for i in range(inicio, final+1):
    ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': ')) #xreeando dicionario y asignandole valores al diccionario
    
print(ventas)