"""
Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de
acordo com a tabela abaixo:

** TABELA NA FOLHA DE EXERCICIOS DA SEÇÃO 5 **
"""

print()
print("Vamos descobrir o IMC de uma pessoa.")

peso = float(input("Digite o peso em Kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do Peso.")
elif 18.6 <= imc <= 24.9:
    print("Saudável.")
elif 25 <= imc <= 29.9:
    print("Peso em excesso.")
elif 30 <= imc <= 34.9:
    print("Obesidade grau I.")
elif 35 <= imc <= 39.9:
    print("Obesidade Grau II (Severa).")
elif imc > 40:
    print("Obesidade Grau III (Mórbida)")

