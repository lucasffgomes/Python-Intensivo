"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo.
"""
from math import ceil

print()

altura_do_degrau = float(input("Altura do degrau da escada em cm: "))
altura_subida = float(input("Altura à subir em cm: "))

qtde_degrau = ceil(altura_subida / altura_do_degrau)  # ceil -> arredonda pra cima
qtde = (altura_subida / altura_do_degrau)

if qtde_degrau > 1:
    print(f"É necessário subir {qtde_degrau} degraus.")
else:
    print(f"É necessário subir {qtde_degrau} degrau.")

# print(f"É necessário subir {qtde_degrau} degraus.")
# print(f"É necessário subir {qtde} degraus.")

