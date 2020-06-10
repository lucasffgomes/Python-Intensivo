"""
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor
lido.
"""

maior_numero = -999
menor_numero = 999

for i in range(0, 5):
    numero = int(input("Digite o número: "))
    if numero > maior_numero:
        maior_numero = numero
    if numero< menor_numero:
        menor_numero = numero

print(f"O maior número é {maior_numero}!")
print(f"O menor número é {menor_numero}!")

