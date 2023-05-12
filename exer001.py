print("Inicio")

for i in range(1,4):
    nome = str(input("Digite o nome do funcionario: "))
    salario = float(input("Digite o salario de: "))
    if salario < 500:
        salario = salario + (salario * 0.15)
    elif salario >= 500 and salario <= 1000:
        salario = salario + (salario * 0.10)
    else:
        salario = salario + (salario * 0.05)
    print("O funcionario: ", nome, ", passa a receber: ", salario)
print("Fim")