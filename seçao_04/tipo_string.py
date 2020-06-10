"""
Tipo string

Em Python um dado é considerado do tipo STRING sempre que:

- Estiver entre aspas simples;          'uma string', '234', 'a', 'True', '42.3'
- Estiver em aspas duplas;              "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas;  '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
- Estiver entre aspas duplas triplas;   ''''''uma string'''''', ''''''234'''''', ''''''a'''''', ''''''True'''''', ''''''42.3''''''

nome = 'Geek University'  TUDO MAIÚSCULA.
print(nome.upper())

nome = 'Geek University'  TUDO MINÚSCULA.
print(nome.lower())

"""

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \n Jolie'  # \n -> Serve para pular linha.
print(nome)
print(type(nome))

nome = """Angelina
Jolie"""
print(nome)
print(type(nome))

print("-----------------------------------------")

nome = "Angelina \" Jolie"  # \" Serve para aparecer a aspas dentro da string na hora de imprimir.
print(nome)

print("-----------------------------------------")

nome = 'Geek University'
print(nome.split())   # SPLIT -> Coloca cada palavra da string em lista.

# [  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14 ]
# [ 'G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y' ]
nome = 'Geek University'
print(nome[0:4])  # Slice de string

print(nome[5:15])  # Slice de string

# [  0,        1]
# ['Geek', 'University']

print(nome.split()[0])
print(nome.split()[1])

print("----------------------------------------------------")

"""
[::-1] -> Começa do primeiro elemento, vá até o último elemnto e inverta.
"""
print(nome[::-1])  # Inversão da STRING Pythônico
# ANTES -> lucas gomes
# DEPOIS -> semog sacul

print(nome.replace('G', 'P'))











