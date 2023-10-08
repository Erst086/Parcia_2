#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:30:41 2023

@author: missael
"""

"""______________________Metodos de ordenamiento_____________________________"""

# Meodo Burbuja

def metodo_burbuja(lista):
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-1):
            if(lista[j]>lista[j+1]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
"""_________________________________________________________________________"""

# Metodo Insercion

def metodo_insercion(lista):
    for j in range(1, len(lista)):
        i = j - 1
        x = lista[j]
        while i >= 0 and x < lista[i]:
            lista[i + 1] = lista[i]
            i -= 1
        lista[i + 1] = x
"""_________________________________________________________________________"""   
     
# Metodo seleccion

def metodo_seleccion(lista):
     n = len(lista)
     for i in range(n - 1):
         minndx = i
         for j in range(i+1,n):
             if(lista[j]<lista[minndx]):
                 minndx = j
         lista[i],lista[minndx]=lista[minndx],lista[i]
"""_________________________________________________________________________"""
             
# Metodo mezcla

def metodo_mezcla (lista):
    if len(lista) <= 1:
        return lista
    # Divide la lista en dos mitades
    mtd = len(lista) // 2
    izq = lista[:mtd]
    der = lista[mtd:]
    # Llama a mergeSort recursivamente en ambas mitades
    izq = metodo_mezcla(izq)
    der = metodo_mezcla(der)
    # Combina (fusiona) las dos mitades ordenadas
    return union(izq, der)

def union(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])  # Agrega los elementos restantes de left
    resultado.extend(der[j:])  # Agrega los elementos restantes de right
    return resultado

"""_________________________________________________________________________"""

#Metodo QuickShor
def metodo_quickshort(lista):
    izq = []
    mtd = []
    der = []
    if len(lista) > 1:
        piv = lista[0]
        for i in lista:
            if i < piv:
                izq.append(i)
            elif i == piv:
                mtd.append(i)
            elif i > piv:
                der.append(i)
        return metodo_quickshort(izq) + mtd + metodo_quickshort(der)
    else:
        return lista
"""
#metodo que presenta problemas en la llamada 
def metodo_quickshort(lista, min, max):
    if min < max:
        piv = parte(lista, min, max)
        metodo_quickshort(lista, min, piv - 1)
        metodo_quickshort(lista, piv + 1, max)

def parte(lista, min, max):
    piv = lista[max]
    i = min - 1
    for j in range(min, max):
        if lista[j] <= piv:
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[max] = lista[max], lista[i + 1]
    return i + 1
"""
 
"""____________________________Llamados main _______________________________"""
lista = []

"""
if __name__ == "__main__":
    

    lista1 = copy.deepcopy(lista)
    lista2 = copy.deepcopy(lista)
    lista3 = copy.deepcopy(lista)
    lista4 = copy.deepcopy(lista)
    lista5 = copy.deepcopy(lista)
    metodo_burbuja(lista1)
    metodo_insercion(lista2)
    metodo_seleccion(lista3)
    lista_ordenada = metodo_mezcla(lista4)
    metodo_seleccion(lista5)

    print("Burbuja   ",lista1)
    print("Insercion ",lista2)
    print("seleccion ",lista3)
    print("Mezcla    ",lista_ordenada)
    print("QuickShort",lista5)
"""