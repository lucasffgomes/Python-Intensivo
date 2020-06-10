"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontados 8% para imposto de renda.
"""

print()
print("Vamos descobrir quanto um encanador recebe.")

preço_do_dia = 30

dias_trabalhado = int(input("Dias trabalhados: "))

quantia_bruta = preço_do_dia * dias_trabalhado

quantia_liquida = quantia_bruta - (quantia_bruta * (8 / 100))

print(f"O encanador trabalhou {dias_trabalhado} dias e receberá R$ {quantia_liquida}.")
print(f"Salário Bruto R$ {quantia_bruta}")
