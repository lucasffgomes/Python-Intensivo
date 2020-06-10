"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = P * 2.54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.
"""

print()
print("Vamos converter o comprimento de POLEGADAS para CENTÍMETROS!")

polegada = float(input("Digite o valor em POLEGADAS: "))

centimetro = polegada * 2.54

print()
print(f"O comprimento em centímetros é {centimetro}cm.")

