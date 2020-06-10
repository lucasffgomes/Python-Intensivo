"""
Faça um programa que receba um número inteiro e verifique se este número é par ou
ímpar.
"""

print()
print("Vamos descobrir se o número é PAR ou ÍMPAR.")

numero = int(input("Digite um número: "))

if numero % 2 == 0:  # resto da divisão
    print("Número PAR")
else:
    print("Número ÍMPAR")

