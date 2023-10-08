#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 18:37:26 2023

@author: zekibestia
"""
from arbol import arbol
ar = arbol()
if __name__ == "__main__":
    estado_inicial=[1,3,2,4]
    solucion=[2,1,3,4]
    nodo_solucion=ar.busqueda_amplitud(estado_inicial,solucion)
    resultado=[]
    nodo=nodo_solucion
    while(nodo.get_padre()!=None):
        resultado.append(nodo.get_datos())
        nodo=nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    