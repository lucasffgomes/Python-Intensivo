"""
Faça um programa que leia um número inteiro positivo N e calcule a soma dos N primeiros
números naturais.
"""

numero = int(input("Digite um número: "))
novo_numero = 0

for i in range(0, numero+1):
    novo_numero = novo_numero + i
print(novo_numero)

