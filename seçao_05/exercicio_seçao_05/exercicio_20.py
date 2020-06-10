"""
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo ESCALENO, EQUILÁTERO ou ISÓSCELE, considerando os seguin-
tes conceitos:
- O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados;
- Chama-se equilátero o triângulo que tem três lados iguais;
- Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais;
- Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""

print()
print("Vamos descobrir se um triângulo é ESCALENO, EQUILÁTERO ou ISÓSCELES.")

lado_a = float(input("Digite o valor do primeiro lado: "))
lado_b = float(input("Digite o valor do segundo lado: "))
lado_c = float(input("Digite o valor do terceiro lado: "))

if lado_a == lado_b and lado_a == lado_c and lado_b == lado_c:
    print("Triângulo Equilátero.")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("Triângulo Isósceles.")
elif lado_a != lado_b or lado_a != lado_c or lado_b != lado_c:
    print("Triângulo Escaleno.")



