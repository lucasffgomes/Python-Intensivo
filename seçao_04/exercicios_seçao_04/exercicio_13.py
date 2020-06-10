"""
Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de
concersão é: M = K / 1.61, sendo K a distância em KM e M em milhas.
"""

print("Vamos converter de QUILÔMETROS para MILHAS.")
print()
kilometro = float(input("Digite a distância em QUILÔMETROS: "))

milha = kilometro / 1.61

print(f"A distância em Milhas será de {milha}mi.")


