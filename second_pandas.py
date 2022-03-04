# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:16:12 2022
"""

import pandas as pd 
import numpy as np

#4. Escribir programa que genere y muestre por pantalla un Data-Frame
#data={'mes': ['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ventas': [30500, 35600, 28300, 33900], 'Gastos':[22000,23400,18100,20700]}
#df=pd.DataFrame(data)
#5. añadiendo nueva columna
#df['Balance']=df['Ventas']-df['Gastos']
#print(df)

#6 Construir una función que construya un DataFrame a partir del un fichero con el formato anterior 
#y devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.

def DataEstadistico():
    df2=pd.read_csv(r'C:\Users\Credd\OneDrive\Documentos\SISTEMAS\PRACTICAS\python\Numpy\cotizacion.csv', sep=';', index_col=0, decimal=',', thousands='.')
    return pd.DataFrame([df2.min(), df2.max(), df2.mean()], index=['Mínimo', 'Máximo', 'Promedio'])

#df is in general

print(DataEstadistico())