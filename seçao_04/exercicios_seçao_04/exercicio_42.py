"""
Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se
que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga
7% de imposto sobre o salário-base.
"""

print()
print("Vamos calcular o salário com gratificação e impostos.")


salario_base = float(input("Digite o salário R$ "))
imposto = salario_base * (7 / 100)
gratificacao = salario_base * (5 / 100)
salario_liquido = (salario_base - imposto) + gratificacao


print(f"O salário bruto será de R$ {salario_base}")
print(f"A gratificação será de R$ {gratificacao}")
print(f"O imposto será de R$ {imposto}")
print()
print(f"O salário líquido será de R$ {salario_liquido}")




