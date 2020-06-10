"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz
quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
"""

print()
print("Vamos descobrir se o número é POSITIVO ou NEGATIVO.")

numero = int(input("Digite um número: "))

if numero > 0:
    raiz = int(numero ** (1/2))
    print(f"O número {numero} é POSITIVO e sua RAIZ QUADRADA é {raiz}.")
elif numero < 0:
    print(f"Número inválido.")
elif numero == 0:
    print("Este é o ZERO.")


