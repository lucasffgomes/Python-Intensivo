"""
Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
trabalhadas no mês. Imprimao valor a ser pago ao funcionário, adicionando 10% sobre
o valor calculado.
"""

print()
print("Vamos descobrir o valor a ser pago com acréscimo de 10%.")

valor_da_hora = float(input("Digite o valor da hora trabalhada R$  "))
horas_trabalhadas = int(input("Digite quantas horas trabalhadas: "))

total = valor_da_hora * horas_trabalhadas

adicional = total + (total * (10 / 100))

print(f"O valor total será de R$ {total}, e com adicional foca {adicional}.")


