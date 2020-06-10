"""
Leia um valor de área em acres e apresente-o convertido em metros quadrados m². A
fórmula de conversão é: M = A * 4048.58, sendo M a área em metros quadrados e A a
área em acres.
"""

print()
print("Vamos converter a área de ACRES para METROS QUADRADOS.")

acre = float(input("Digite a área em ACRES: "))

metro_quadrado = acre * 4048.58

print(f"O valor de área em METROS QUADRADOS é de {metro_quadrado}m².")

