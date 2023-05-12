primeiroProduto = float(input("Qual o valor do primeiro produto:  "))
segundoProduto = float(input("Qual o valor do segundo produto: "))

porcentagem1 = primeiroProduto * 0.14
porcentagem2 = segundoProduto * 0.17
desc1 = primeiroProduto - porcentagem1
desc2 = segundoProduto - porcentagem2

print("O primeiro produto tem o valor de: " , primeiroProduto , " reais, e recebeu o desconto de 14%, com valor final de: " , desc1)
print("O segundo produto tem o valor de: " , segundoProduto , " reais, e recebeu o desconto de 17%, com valor final de: " , desc2)  
print("O 1 recebeu um desconto de: ", porcentagem1, "reais")    
print("O 2 recebeu um desconto de: ", porcentagem2, "reais") 