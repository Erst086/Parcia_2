#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 21:29:19 2023

@author: missael
"""

import csv
import random

# Nombre del archivo CSV
nombre_archivo = "datos_150k.csv"

# Abre el archivo CSV en modo escritura
with open(nombre_archivo, mode='w', newline='') as archivo_csv:
    # Define el encabezado del archivo CSV
    encabezado = ['numero', 'valor']

    # Crea el escritor CSV
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezado)

    # Escribe el encabezado en el archivo
    escritor_csv.writeheader()

    # Genera un millón de filas de datos
    for numero in range(1, 10000):
        valor = random.randint(1, 2000000)
        escritor_csv.writerow({'numero': numero, 'valor': valor})

print(f"Se ha generado el archivo CSV '{nombre_archivo}' con N numero de datos.")
