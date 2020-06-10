"""
Leia um valor de massa em quilogramas a apresente-o convertido em libras. A fórmula
de conversão é: L = K / 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""

print()
print("Vamos converter a massa de QUILOGRAMA para LIBRA!")

quilograma = float(input("Digite a massa em QUILOGRAMA: "))

libra = quilograma / 0.45

print(f"O valor convertido em LIBRA é de {libra}.")