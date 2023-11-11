#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:21:33 2023

@author: missael
"""

import metodos_ordenamientos
import pandas as pd
"""

Los archivos de lectura son datos_150k que contiene 150000 datos

"""
"""__________________________Llamada y letura_______________________________""" 
def leer_csv_obtener_valores(nombre_archivo):
    try:
        # Leer el archivo CSV en un DataFrame de Pandas
        df = pd.read_csv(nombre_archivo)
        
        # Obtener los valores de la columna "valor" como una lista
        valores = df['valor'].tolist()
        
        return valores
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        return []


"""_________________________Metodos en general______________________________"""


def ordenar_y_guardar_csv(metodo_ordenamiento, nombre_archivo_entrada, nombre_archivo_salida):
    # Leer el archivo CSV y obtener los valores
    lista = leer_csv_obtener_valores(nombre_archivo_entrada)
    
    # Aplicar el método de ordenamiento deseado
    metodo_ordenamiento(lista)
    
    # Crear un nuevo DataFrame con los valores ordenados
    df_ordenado = pd.DataFrame({'valor_ordenado': lista})
    
    # Guardar el DataFrame como un archivo CSV
    df_ordenado.to_csv(nombre_archivo_salida, index=False)
    
    print(f"Valores ordenados con '{metodo_ordenamiento.__name__}' guardados en '{nombre_archivo_salida}'")

# Ejemplo de uso para el método de burbuja
nombre_archivo_entrada = "datos_150k.csv"
nombre_archivo_salida = "datos_ordenados_burbuja.csv"
ordenar_y_guardar_csv(metodos_ordenamientos.metodo_burbuja, nombre_archivo_entrada, nombre_archivo_salida)

# Ejemplo de uso para el método de inserción
nombre_archivo_entrada = "datos_150k.csv"
nombre_archivo_salida = "datos_ordenados_insercion.csv"
ordenar_y_guardar_csv(metodos_ordenamientos.metodo_insercion, nombre_archivo_entrada, nombre_archivo_salida)

# Ejemplo de uso para el método de selección
nombre_archivo_entrada = "datos_150k.csv"
nombre_archivo_salida = "datos_ordenados_seleccion.csv"
ordenar_y_guardar_csv(metodos_ordenamientos.metodo_seleccion, nombre_archivo_entrada, nombre_archivo_salida)




def leer_csv_obtener_valores_M(nombre_archivo):
    try:
        # Leer el archivo CSV en un DataFrame de Pandas
        df = pd.read_csv(nombre_archivo)
        # Obtener los valores de la columna "valor" como una lista
        valores = df['valor'].tolist()
        return valores
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        return []

nombre_archivo = "datos_150k.csv"
lista = leer_csv_obtener_valores_M(nombre_archivo)
valores_ordenados = metodos_ordenamientos.metodo_mezcla(lista)
# Crear un nuevo DataFrame con los valores ordenados
df_ordenado = pd.DataFrame({'valor_ordenado': valores_ordenados})
# Guardar el DataFrame como un archivo CSV
nombre_archivo_ordenado = "datos_ordenados_mezcla.csv"
df_ordenado.to_csv(nombre_archivo_ordenado, index=False)

print(f"Valores ordenados con 'metodo_mezcla' guardados en'{nombre_archivo_ordenado}'")




def leer_csv_obtener_valores_QKS(nombre_archivo):
    try:
        # Leer el archivo CSV en un DataFrame de Pandas
        df = pd.read_csv(nombre_archivo)
        # Obtener los valores de la columna "valor" como una lista
        valores = df['valor'].tolist()
        return valores
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        return []

nombre_archivo = "datos_150k.csv"
lista = leer_csv_obtener_valores_QKS(nombre_archivo)
resultado_quicksort = metodos_ordenamientos.metodo_quickshort(lista)
# Crear un nuevo DataFrame con los valores ordenados
df_ordenado = pd.DataFrame({'valor_ordenado': resultado_quicksort})
# Guardar el DataFrame como un archivo CSV
nombre_archivo_ordenado = "datos_ordenados_quickshort.csv"
df_ordenado.to_csv(nombre_archivo_ordenado, index=False)

print(f"Valores ordenados con 'metodo_quickshort' guardados en'{nombre_archivo_ordenado}'")

