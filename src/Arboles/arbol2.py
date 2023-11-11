#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:30:36 2023

@author: zekibestia
"""
from Nodo import Nodo
class arbol2:
 def busqueda_amplitud(self,estado_inicial,solucion):
    solucionado=False
    nodos_visitados=[]
    nodos_pendientes=[]
    nodoInicial=Nodo(estado_inicial)
    nodos_pendientes.append(nodoInicial)
    while((not solucionado) and (len(nodos_pendientes)!=0)):
        nodo=nodos_pendientes.pop(0)
        # Extrae el nodo de pendientes y lo agrega a visitantes
        nodos_visitados.append(nodo)
        if(nodo.get_datos()==solucion):
            solucionado=True
            return nodo
        else:
            dato_nodo=nodo.get_datos()
            # Numeros {1,2,3,4,5,6}
            #Operacion izquierda {x,x,3,4,5,6}
            hijo=[dato_nodo[1],dato_nodo[0],dato_nodo[2],dato_nodo[3],dato_nodo[4],dato_nodo[5]]
            hijo_izq=Nodo(hijo)
            if((not hijo_izq.en_lista(nodos_pendientes))
               and (not hijo_izq.en_lista(nodos_visitados))):
                nodos_pendientes.append(hijo_izq)
            #Operacion centro {1,2,x,x,5,6}
            hijo=[dato_nodo[0],dato_nodo[1],dato_nodo[3],dato_nodo[2],dato_nodo[4],dato_nodo[5]]
            hijo_centro=Nodo(hijo)
            if((not hijo_centro.en_lista(nodos_pendientes)) and
            (not hijo_centro.en_lista(nodos_visitados))):
                nodos_pendientes.append(hijo_centro)
            #Operacion derecho {1,2,3,4,x,x}
            hijo=[dato_nodo[0],dato_nodo[1],dato_nodo[2],dato_nodo[3],dato_nodo[5],dato_nodo[4]]
            hijo_derecho=Nodo(hijo)
            if((not hijo_derecho.en_lista(nodos_pendientes)) and
            (not hijo_derecho.en_lista(nodos_visitados))):
                nodos_pendientes.append(hijo_derecho)
            nodo.set_hijos([hijo_izq,hijo_centro,hijo_derecho])
