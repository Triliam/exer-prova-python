nome = str(input("Qual o nome? "))
soma = 0.0
qtdNotas = 5

for i in range(qtdNotas):
    nota = float(input("Qual a nota ? "))
    soma = soma + nota

media = soma/qtdNotas

if media > 7:
    print("Parabéns ", nome, "! Você foi aprovado!")
elif media >= 5 and media < 7:
    print("Você ficou com média: ", media, ". E ficou de recuperação.")
else:
    print(nome, ", você foi reprovado.")

print("")