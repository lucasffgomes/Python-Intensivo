"""
Usando Switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
correspondente a este número. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.
"""

print()
print("Vamos descobrir os meses.")

numero = int(input("Digite um número de 1 à 12: "))

if numero < 1 or numero > 12:
    print("Número inválido.")

elif numero == 1:
    print("Janeiro.")
elif numero == 2:
    print("Fevereiro.")
elif numero == 3:
    print("Março.")
elif numero == 4:
    print("Abril.")
elif numero == 5:
    print("Maio.")
elif numero == 6:
    print("Junho.")
elif numero == 7:
    print("Julho.")
elif numero == 8:
    print("Agosto.")
elif numero == 9:
    print("Setembro.")
elif numero == 10:
    print("Outubro.")
elif numero == 11:
    print("Novembro.")
elif numero == 12:
    print("Dezembro.")

