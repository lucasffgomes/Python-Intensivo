"""
Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos
três valores lidos.
"""

valor1 = int(input("Digite o primeiro valor: "))
#valor1 ** 2
print(f"O QUADRADO do primeiro valor {valor1}².")

print()
valor2 = int(input("Digite o segundo valor: "))
print(valor2 ** 2)

print()
valor3 = int(input("Digite o terceiro valor: "))
print(valor3 ** 2)

resultado = (valor1 ** 2) + (valor2 ** 2) + (valor3 ** 2)

print(f"A soma dos quadrados dos valores é {resultado}")




