# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 23:09:22 2023

@author: Zeki
"""
class MetodosMatematicos:
    @staticmethod
    def suma_recursiva(n):
        if n == 0:
            return 0
        else:
            return n + MetodosMatematicos.suma_recursiva(n - 1)

    @staticmethod
    def fibonacci_recursivo(n):
        if n <= 1:
            return n
        else:
            return MetodosMatematicos.fibonacci_recursivo(n - 1) + MetodosMatematicos.fibonacci_recursivo(n - 2)

    @staticmethod
    def fibonacci_iterativo(n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    @staticmethod
    def suma_digitos_recursiva(numero):
        if numero == 0:
            return 0
        else:
            return numero % 10 + MetodosMatematicos.suma_digitos_recursiva(numero // 10)

    @staticmethod
    def sumaCadenas(n):
        if len(n) == 1:
            return int(n)
        else:
            return int(n[0]) + MetodosMatematicos.sumaCadenas(n[1:])
    @staticmethod  
    def busqueda_binaria(arr, objetivo):
     izquierda, derecha = 0, len(arr) - 1

     while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

     return -1
 
resultado_suma = MetodosMatematicos.suma_recursiva(5)
print("Suma recursiva:", resultado_suma)

resultado_fib = MetodosMatematicos.fibonacci_recursivo(10)
print("Fibonacci recursivo:", resultado_fib)

resultado_suma_digitos = MetodosMatematicos.suma_digitos_recursiva(9876)
print("Suma de dígitos:", resultado_suma_digitos)

resultado_busqueda = MetodosMatematicos.busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15], 9)
print("Búsqueda binaria:", resultado_busqueda)



