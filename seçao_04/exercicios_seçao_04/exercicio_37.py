"""
Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%.
"""

print()
print("Vamos descobrir o valor de um produto com desconto.")

valor_original = float(input("Digite o valor do produto R$ "))

valor_com_desconto = valor_original - ((valor_original * 12) / 100)

print(f"O produto com desconto custará R$ {valor_com_desconto}")



