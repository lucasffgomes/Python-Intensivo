"""
Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua
média.
"""

print("Vamos calcular a média dos números positivos.")

soma = 0
contador = 0

for i in range(0, 10):
    contador += 1
    numero = int(input("Digite o número: "))
    soma += numero

print(soma)


