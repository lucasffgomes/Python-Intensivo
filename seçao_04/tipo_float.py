"""
Tipo FLOAT

Tipo real, decimal

Casas decimais
OBS: O separador de casa decimais é o ponto e não a vírgula.
"""

# ERRADO do ponto de vista do FLOAT, mas gera uma TUPLA.
valor = 1, 44
print(valor)
print(type(valor))

# CERTO do ponto de vista FLOAT.
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição.
valor1, valor2 = 2, 88
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um FLOAT em INT
"""
OBS: Ao converter valores float para inteiros, nós perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j













