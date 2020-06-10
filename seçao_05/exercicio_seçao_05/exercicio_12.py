"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número
inválido". Se o número for positivo, calcular o logaritmo deste número.
"""
import math

print()
print("Vamos ler um número.")

numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print("Número inválido.")
elif numero > 0:
    numero = math.log(numero, 10)  # math.log(VARIAVEL, BASE)
    print(numero)


