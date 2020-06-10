"""
Recebendo dados do USUÁRIO

input() -> Todo dado recebido via input é do tipo STRING

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

"""

# Entrada de dados
# print("Qual seu nome? ")
# nome = input()  # input -> Entrada

nome = input("Qual seu nome? ")

# Exemple de print 'antigo' 2.x
# print("Seja bem-vindo(a) %s" % nome)

# Exemple de print 'moderno' 3.x
# print('Seja bem-vindo(a)1 {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome.title()}!')  # title -> deixar a primeira letra MAIÚSCULA

# print("Qual sua idade?")
# idade = input()

idade = int(input("Quantos anos? "))  # O int altera o tipo de string para inteiro.

# Processamento

# Saída de dados
# Exemple de print 'antigo' 2.x
# print("O %s tem %s anos" % (nome, idade))

# Exemple de print 'moderno' 3.x
# print("O {0} tem {1} anos.".format(nome, idade))

print(f"O {nome.title()} tem {idade} anos.")  # title -> deixar a primeira letra MAIÚSCULA


"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""

# print(f'O {nome.title()} nasceu em {2019 - int(idade)}')  # conversao em int


"""---------------------RESUMO--------------------------"""

nome = input("Qual seu nome? ")
print(f'Seja bem-vindo(a) {nome.title()}!')

idade = int(input("Quantos anos? "))
print(f"O {nome.title()} tem {idade} anos.")


