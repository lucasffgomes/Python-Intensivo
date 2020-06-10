"""
Faça um programa que peça ao usuário para digitar 10 valores e some-os.
"""

print("Vamos calcular a soam de 10 valores.")

resultado = 0

for vez in range(0, 10):
    valor = int(input("Digite o valor: "))
    resultado += valor

print(resultado)

