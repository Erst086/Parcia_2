#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 17:16:54 2023

@author: zekibestia
"""

class Nodo:
    def __init__(self,datos,hijos=None):
        self.datos=datos
        self.hijos=hijos
        self.padre=None
    def set_hijos(self,hijos):
        self.hijos=hijos
        if(self.hijos!=None):
            for hij in self.hijos:
                hij.padre=self
    def get_hijos(self):
        return self.hijos
    def set_padre(self,padre):
        self.padre=padre
    def get_padre(self):
        return self.padre
    def set_datos(self,datos):
        self.datos=datos
    def get_datos(self):
        return self.datos
    def igual(self,nodo):
        if(self.get_datos()==nodo.get_datos()):
            return True
    def en_lista(self,lista_nodos):
        esta_en_lista=False
        for n in lista_nodos:
            if self.igual(n):
                esta_en_lista=True
                break
        return esta_en_lista
    def __str__(self):
        return str(self.get_datos())
    