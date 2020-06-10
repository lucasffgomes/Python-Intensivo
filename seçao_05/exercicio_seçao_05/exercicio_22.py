"""
Leia  a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se
aposentar. As condições para aposentadoria são:
- Ter pelo 65 anos;
- Ou ter trabalhado pelo menos 30 anos;
- Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""

print()
print("Vamos descobrir se um trabalhador pode se aposentar.")

idade = int(input("Digite a idade: "))
tempo_de_servico = int(input("Digite o tempo de serviço: "))

if idade >= 65 or tempo_de_servico >= 30:
    print("Pode aposentar.")

elif idade >= 60 and tempo_de_servico >= 25:
    print("Vai se aposentar com 60 anos.")

else:
    print("Vai trabalhar maluco!!!")



