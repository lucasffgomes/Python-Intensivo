"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os números
pares de 0 até N em ordem crescente.
"""

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    for i in range(0, numero + 1, 2):
        print(i)
