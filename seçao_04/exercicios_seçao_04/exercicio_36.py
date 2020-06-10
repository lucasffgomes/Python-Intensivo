"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
de um um cilindro circular é calculado por meio da seguinte fórmula: V = π * raio² * altura,
onde π = 3.141592.
"""

print()
print("Vamos calcular o VOLUME de um cilindro.")

raio = float(input("Digite o valor do raio da base do cilindro: "))
altura = float(input("Digite o valor da altura do cilindro: "))

π = 3.141592

volume = π * (raio ** 2) * altura

print(f"O VOLUME do cilindro será de: {volume}m³.")


