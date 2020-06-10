"""
Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de
sua idade e do ano atual.
"""

print()
print("Vamos descobrir a idade da pessoa.")

ano_de_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_de_nascimento

print(f"A pessoa tem {idade} anos.")