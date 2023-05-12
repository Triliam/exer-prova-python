print("Inicio")

altura = float(input("Altura: "))
peso = float(input("Peso: "))
imc = peso /(altura * altura)

if imc < 18.5:
    print("Abaixo")
elif imc > 18.5 and imc < 25:
    print("Normal")
elif imc > 25 and imc < 30:
    print("Sobrepso")
else:
    print("Obesidade")
print("Fim")