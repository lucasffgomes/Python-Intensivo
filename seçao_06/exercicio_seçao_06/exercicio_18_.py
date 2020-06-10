"""
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e
quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser
fornecida pelo usuário.
"""

qtde_numeros = int(input("Digite a quantidade de números: "))
maior_numero = -999
contador = 0

for i in range(1, qtde_numeros+1):
    numero_lido = int(input(f"Digite o {i}º valor: "))
    if numero_lido > maior_numero:
        maior_numero = numero_lido
        if maior_numero == numero_lido:
            contador += 1

print(f"O maior número é {maior_numero}, e aparece {contador} vezes.")
