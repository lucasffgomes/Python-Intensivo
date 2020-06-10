"""
Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os
números ímpares de 1 até N em ordem decrescente.
"""

numero = int(input("Digite um número: "))

if numero % 2 != 0:
    for i in range(numero, 0, -2):
        print(i)

