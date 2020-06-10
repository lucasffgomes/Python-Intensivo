"""
Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
números forem iguais, imprima a mensagem NÚMEROS IGUAIS.
"""

print()
print("Vamos descobrir qual número é maior.")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"O número {numero1} é maior que o número {numero2}.")
elif numero2 > numero1:
    print(f"O número {numero2} é maior que o número {numero1}.")
else:
    print("Números iguais.")
