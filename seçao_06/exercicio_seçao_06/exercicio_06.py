"""
Faça um programa que leia 10 inteiros e imprima sua média.
"""

print("Vamos descobrir a média.")

contador = 0
resultado = 0

for i in range(0, 10):
    contador = contador + 1
    valor = int(input(f"Digite o {contador}º valor: "))
    resultado = resultado + valor

print(f"A média final será {resultado/contador}")


