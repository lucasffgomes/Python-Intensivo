"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
prestação for maior que 20% do salário imprima: EMPRÉSTIMO NÃO CONCEDIDO, caso
contrário imprima: EMPRÉSTIMO CONCEDIDO.
"""

print()
print("Vamos descobrir se ocorrerá o empréstimo.")

salario = int(input("Digite o salário: "))
emprestimo = int(input("Digite o valor do empréstimo: "))

if emprestimo > (salario * (20 / 100)):
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")
