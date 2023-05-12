

soma = 0.0
qtdNotas = 5

for i in range(qtdNotas):
    nota = float(input("Qual a nota ? "))
    soma = soma + nota
    print(i)

media = soma/qtdNotas
if media > 7:
    print("Aprovado")
else:
    print("Reprovado")
    

print("A média é: ", media)