"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e
a segunda prova tem peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno
e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou
superior a 60 pontos.
"""

print()
print("Vamos descobrir a média ponderada.")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_ponderada = ((nota1 * 1) + (nota2 * 1) + (nota3 * 2)) / (1 + 1 + 2)

print(f"A média ponderada será de {media_ponderada} pontos.")

if media_ponderada > 6:
    print("Aluno APROVADO!")
else:
    print("Aluno REPROVADO!")


