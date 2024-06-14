base = float(input("Digite o valor da base do triângulo: "))

while base <= 0:
    print("Erro: A base do triângulo deve ser maior que zero.")
    base = float(input("Digite novamente o valor da base do triângulo: "))

altura = float(input("Digite o valor da altura do triângulo: "))

while altura <= 0:
    print("Erro: A altura do triângulo deve ser maior que zero.")
    altura = float(input("Digite novamente o valor da altura do triângulo: "))

area = (base * altura) / 2
print("A área do triângulo é:", area)