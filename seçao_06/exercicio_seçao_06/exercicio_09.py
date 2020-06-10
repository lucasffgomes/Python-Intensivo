"""
Faça um programa que leia um número inteiro N e depois imprima os N primeiros
números naturais ímpares.
"""

numero = int(input("Digite um número: "))

for i in range(0, numero):
    if i % 2 == 0:
        print(f"{i} é par")
    # else:
    #    print(f"{i} é ímpar")

