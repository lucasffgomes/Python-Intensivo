"""
Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se
for divisível por 400 ou se for divisível por 4 e não for divisível por 100.
Por exemplo: 1988, 1992, 1996.
"""

print()
print("Vamos descobrir se o ano é bissexto.")

ano = int(input("Digite um ano válido: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO.")
else:
    print("Não é bissexto.")


