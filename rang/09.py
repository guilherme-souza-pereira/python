#Exemplo 9
#Com o uso do while:
# Recebendo o número do usuário:
Inumero = input("digite um número para o cálculo de sua tabuada: \n")
# Convertendo o número para inteiro:
numero = int(Inumero)
# Criando a variável de controle do laço de repetição
contador = 1
while(contador<=10):
# Exibindo o valor da tabuada:
    print(f" {numero} x {contador} = {numero*contador}")
    contador = contador + 1
print ("Fim de programa!")
#Exemplo 10 (Uso dos acumuladores)
# Para esse exemplo vamos criar um programa que cálcula a média das idades de 5 pessoas.
# Criando a variável de controle do laço, contando 5 repetições
contador = 1
# Criando uma variável para acumular os valores das idades digitadas:
soma = 0
# Criando o laço de repetição para receber 5 idades e somá-las:
while (contador<=5):
# Recebendo a idade do usuário
    idade = int(input(f"Digite a idade do usuário nº{contador}: "))
# somando a idade do usuário ao valor atual da variável acumulador
    #soma = soma + idade
    soma += idade
# incrementando a variável contador para controle do laço
    #contador = contador + 1
    contador += 1
# calculando a média das idades:
media = soma/ (contador-1)
print(f"A média das idades digitadas é igual: {media}")
