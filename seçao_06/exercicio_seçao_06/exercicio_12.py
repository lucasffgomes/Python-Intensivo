"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números
naturais de 0 até N em ordem decrescente.
"""

numero = int(input("Digite um número: "))

for i in range(numero, 0, -1):  # (-1) - INVERTE A ORDEM
    print(i)
