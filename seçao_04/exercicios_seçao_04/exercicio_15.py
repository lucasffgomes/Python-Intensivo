"""
Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é: G = R * 180 / π, sendo G o ângulo em graus e R em radianos e π = 3.14.
"""

print("Vamos converter de RADIANOS para GRAUS!")

radianos = float(input("Digite um valor em Radianos: "))

π = 3.14

graus = (radianos * 180) / π

print(f"O valor do ângulo em graus é {graus}.")


