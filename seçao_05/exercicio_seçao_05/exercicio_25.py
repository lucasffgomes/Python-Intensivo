"""
Calcule as raízes da equação de 2º grau.
Lembrando que:
X = (-b +- (delta * (1/2)) / (2 * a)

Onde:
delta = b² - 4ac

E ax² + bx + c = 0 representa uma equação de 2º grau.

A variável (a) tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Não
é equação de segundo grau".
- Se DELTA < 0, não existe real. Imprima a mensagem não existe raiz.
- Se DELTA = 0, exite uma raiz. Imprima a raiz e a mensagem raíz única.
- Se DELTA >= 0, imprima as duas raízes reais.
"""

print()
print("Vamos resolver uma equação de Segundo Grau.")

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

DELTA = (b ** 2) - (4 * a * c)

print(f"O valor de delta é: {DELTA}")

if DELTA < 0:
    print("Não existe raiz.")

elif DELTA == 0:
    print("Raízes iguais.")

    X1 = ((-b) + (DELTA ** (1/2))) / (2 * a)
    X2 = ((-b) - (DELTA ** (1/2))) / (2 * a)
    print(f"E seu resultado é X1 = {int(X1)} e X2 = {int(X2)}")

elif DELTA > 0:
    print("Existem duas raízes diferentes.")
    X1 = ((-b) + (DELTA ** (1/2))) / (2 * a)
    X2 = ((-b) - (DELTA ** (1/2))) / (2 * a)
    print(X1)
    print(X2)










