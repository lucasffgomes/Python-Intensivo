"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
peso ideal, utilizando as seguintes fórmulas (onde H corresponde à altura):
- Homens: (72,7 * H) - 58
- Mulheres: (62,1 * H) - 44,7
"""

print()
print("Vamos calcular o peso ideal.")

altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo, M ou F: ")

if sexo == "M":
    peso_masc = (72.7 * altura) - 58
    print(f"O peso ideal para o sexo masculino é de {peso_masc}Kg.")
elif sexo == "F":
    peso_femi = (62.1 * altura) - 44.7
    print(f"O peso ideal para o sexo feminino é de {peso_femi}Kg.")
else:
    print("NdA.")


