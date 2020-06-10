"""
Leia um salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que
ele recebeu um aumento de 25%.
"""

print()
print("Vamos descobrir o valor do novo salário com reajuste.")

salario = float(input("Digite o valor do seu salário R$ "))
aumento = int(input("Digite a porcentagem de aumento: "))

novo_salario = salario + ((salario * aumento) / 100)

reajuste = novo_salario - salario

print(f"O novo salário será de R$ {novo_salario}")
print(f"O reajuste foi de R$ {reajuste}")