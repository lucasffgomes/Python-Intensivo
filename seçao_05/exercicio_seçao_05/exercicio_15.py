"""
Usando Switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e
assim por diante.
"""

print()
print("Vamos descobrir o dia da semana.")

numero = int(input("Digite um número de 1 à 7; "))

if numero < 1 or numero > 7:
    print("Número inválido!")

elif numero == 1:
    print("Domingo.")
elif numero == 2:
    print("Segunda-feira.")
elif numero == 3:
    print("Terça-feira.")
elif numero == 4:
    print("Quarta-feira.")
elif numero == 5:
    print("Quinta-feira.")
elif numero == 6:
    print("Sexta-feira.")
elif numero == 7:
    print("Sábado.")


