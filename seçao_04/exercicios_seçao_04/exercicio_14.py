"""
Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R = G * π / 180, sendo G o ângulo em graus e R em radianos e π = 3.14
"""

print("Vamos transformar de Graus para Radianos!")

grau = float(input("Digite um valor em Graus: "))

π = 3.14

radiano = grau * π / 180

print()
print(f"O valor em Radianos será de {radiano}.")


