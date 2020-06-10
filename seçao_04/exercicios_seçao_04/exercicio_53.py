"""
Faça um programa para ler as dimensões de um terreno (comprimento C e largura L),
bem como o preço do metro de tela P. Imprima o custo para cercar este mesmo terreno
com tela.
"""
from math import ceil

print()
print("Vamos descobrir as dimensões do terreno e o custo para cercar.")

comprimento_terreno = int(input("Digite o comprimento em metros: "))
largura_terreno = int(input("Digite a largura em metros: "))

area_total = comprimento_terreno * largura_terreno
perimetro_total = (2 * comprimento_terreno) + (2 * largura_terreno)

print(f"A área total do terreno será de {area_total}m² e seu perímetro será de {perimetro_total}m")

tela_por_metro = float(input("Digite o valor de tela por metro: R$ "))

custo_total = (perimetro_total * tela_por_metro)

print(f"O custo para cercar o terreno será de R$ {custo_total}.")

