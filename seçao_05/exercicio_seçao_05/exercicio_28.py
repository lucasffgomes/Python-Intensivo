"""
Faça um programa que leia três números positivos e efetue o cálculo de uma das
seguintes médias de acordo com um valor numérico digitado pelo usuário:

A) GEOMÉTRICA
B) PONDERADA
C) HARMÔNICA
D) ARITMÉTICA
"""

print("Vamos calcular as médias.")
print()

x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))
z = int(input("Digite o valor de Z: "))

print("Tipos de média.")
print("1> GEOMÉTRICA.")
print("2> PONDERADA.")
print("3> HARMÔNICA.")
print("4> ARTIMÉTICA.")

tipo_de_media = int(input("Digite o tipo de média correspondente: "))

if tipo_de_media == 1:
    print("Média Geométrica.")
    resultado = (x * y * z) ** (1/3)
    print(f"O resultado é {resultado}")

elif tipo_de_media == 2:
    print("Média Ponderada.")
    resultado = (x + (2 * y) + (3 * z)) / 6
    print(f"O resultado é {resultado}")

elif tipo_de_media == 3:
    print("Média Harmônica.")
    resultado = 1 / ((1/x) + (1/y) + (1/z))
    print(f"O resultado é {resultado}")

elif tipo_de_media == 4:
    print("Média Aritmética.")
    resultado = (x + y + z) / 3
    print(f"O resultado é {resultado}")

else:
    print("Digite uma opção válida.")














