#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:21:33 2023

@author: missael
"""

import metodos_ordenamientos
import pandas as pd
import time
import matplotlib.pyplot as plt
import copy

class Ordenamiento:
    @staticmethod
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

    @staticmethod
    def ordenar_y_guardar_csv(metodo_ordenamiento, nombre_archivo_entrada, nombre_archivo_salida):
        # Leer el archivo CSV y obtener los valores
        lista = Ordenamiento.leer_csv_obtener_valores(nombre_archivo_entrada)
        # Aplicar el método de ordenamiento deseado
        metodo_ordenamiento(lista)
        # Crear un nuevo DataFrame con los valores ordenados
        df_ordenado = pd.DataFrame({'valor_ordenado': lista})
        # Guardar el DataFrame como un archivo CSV
        df_ordenado.to_csv(nombre_archivo_salida, index=False)
        print(f"Valores ordenados con '{metodo_ordenamiento.__name__}' guardados en '{nombre_archivo_salida}'")

    @staticmethod
    def tiempo_ejecucion(metodo, nombre_metodo, datos):
        inicio = time.time()  # Registrar el tiempo de inicio
        metodo(datos)  # Aplicar el método de ordenamiento
        fin = time.time()  # Registrar el tiempo al finalizar el método
        tiempo_ejecucion = fin - inicio  # Calcular el tiempo de ejecución
        print(f"Tiempo de ejecución de '{nombre_metodo}': {tiempo_ejecucion} segundos")
        return tiempo_ejecucion

    @staticmethod
    def plot_progress(metodo, nombre_metodo, datos):
        datos_ordenados = copy.deepcopy(datos)  # Copia de los datos originales
        n = len(datos_ordenados)
        for i in range(n):
            metodo(datos_ordenados)
            plt.bar(range(n), datos_ordenados)  # Utiliza plt.bar() para gráfico de barras
        plt.xlabel('Índice')
        plt.ylabel('Valor')
        plt.title(f'Progreso de {nombre_metodo}')
        plt.show()
    @staticmethod
    def mostrar_orden(nombre_ordenamiento, datos):
        datos_ordenados = sorted(datos) if nombre_ordenamiento == 'Merge Sort' else metodos_ordenamientos.metodo_quickshort(datos)

        plt.bar(range(len(datos_ordenados)), datos_ordenados)
        plt.xlabel('Índice')
        plt.ylabel('Valor')
        plt.title(f'Progreso final de {nombre_ordenamiento}')
        plt.show()
if __name__ == "__main__":
    nombre_archivo = 'datos_50.csv'

    Ordenamiento.ordenar_y_guardar_csv(metodos_ordenamientos.metodo_burbuja, nombre_archivo, "datos_ordenados_burbuja.csv")
    Ordenamiento.ordenar_y_guardar_csv(metodos_ordenamientos.metodo_insercion, nombre_archivo, "datos_ordenados_insercion.csv")
    Ordenamiento.ordenar_y_guardar_csv(metodos_ordenamientos.metodo_seleccion, nombre_archivo, "datos_ordenados_seleccion.csv")

    datos = Ordenamiento.leer_csv_obtener_valores(nombre_archivo)

    Ordenamiento.tiempo_ejecucion(metodos_ordenamientos.metodo_quickshort, "método_quickshort", datos)
    Ordenamiento.tiempo_ejecucion(metodos_ordenamientos.metodo_mezcla, "método_mezcla", datos)
    
    Ordenamiento.tiempo_ejecucion(metodos_ordenamientos.metodo_burbuja, "método burbuja", datos[:])  # Utiliza una copia de datos
    Ordenamiento.tiempo_ejecucion(metodos_ordenamientos.metodo_insercion, "método inserción", datos[:])
    Ordenamiento.tiempo_ejecucion(metodos_ordenamientos.metodo_seleccion, "método selección", datos[:])

    Ordenamiento.plot_progress(metodos_ordenamientos.metodo_burbuja, "método burbuja", datos[:])
    Ordenamiento.plot_progress(metodos_ordenamientos.metodo_insercion, "método inserción", datos[:])
    Ordenamiento.plot_progress(metodos_ordenamientos.metodo_seleccion, "método selección", datos[:])
    
    Ordenamiento.mostrar_orden('Quicksort', datos)
    Ordenamiento.mostrar_orden('Merge Sort', datos)
