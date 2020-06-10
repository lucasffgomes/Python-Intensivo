"""
A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
- O primeiro ganhador receberá 46%;
- O segundo receberá 32%;
- O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

print()
print("Vamos calcular quanto cada vencedor ganhou.")

valor = float(input("Digite a quantia do concurso R$ "))


ganhador1 = valor * (46 / 100)
print(f"O ganhador 1 recebeu R$ {ganhador1}")

ganhador2 = valor * (32 / 100)
print(f"O ganhador 2 recebeu R$ {ganhador2}")

ganhador3 = valor - (ganhador1 + ganhador2)
print(f"O ganhador 3 recebeu R$ {ganhador3}")

soma = ganhador1 + ganhador2 + ganhador3

print(f"A soma dos valores dos ganhadores é de {soma}")



