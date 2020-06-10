"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das
seguintes categorias:
CATEGORIA   |  IDADE
Infantil A  |  5 a 7
Infantil B  |  8 a 10
Juvenil A   |  11 a 13
Juvenil B   |  14 a 17
Sênior      |  maiores de 18 anos
"""

print()
print("Vamos descobrir o nível do nadador pela idade.")

idade = int(input("Digite a idade do nadador: "))

if 5 <= idade <= 7:
    print("O nadador é da categoria Infantil A.")
elif 8 <= idade <= 10:
    print("O nadador está na categoria Infantil B.")
elif 11 <= idade <= 13:
    print("O nadador está na categoria Juvenil A.")
elif  14 <= idade <= 17:
    print("O nadador está na categoria Juvenil B.")
elif idade >= 18:
    print("O nadador está na categoria Sênior.")
else:
    print("Muito novo para nadar.")

