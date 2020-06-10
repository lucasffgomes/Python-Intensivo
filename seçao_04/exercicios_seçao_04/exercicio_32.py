"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de
seu dobro.
"""

print()
print("Vamos raciocinar um pouquinho.")

numero = int(input("Digite um número inteiro: "))

triplo = numero * 3
dobro = numero * 2

resultado = (triplo + 1) + (dobro - 1)

print(f"A resposta é: {resultado}.")




