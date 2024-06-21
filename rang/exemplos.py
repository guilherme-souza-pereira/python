#Exemplo 1
for cont in range(10):
    print(cont)

#Exemplo 2
for i in range (10):
    print("The value of i is currently", i)

#Exemplo 3
#Fazer a Tabuada 0 - 10 com for
n = int(input())
for i in range (11):
   print(n, "X", i, "=", n*i)

#Exemplo 4
# Range(inicio,final,incremento)
for cont in range(0,10,1):
    print(cont)

#Exemplo 5
#Fazer a Tabuada 0 - 20 com for, mas somente 0 5 10 15 20 (i incrementar 5 )
n = int(input())
for i in range (0, 21, 5):
    print(n, "X", i, "=", n*i)


#Exemplo 6
for i in range(10,0,-1):
    print(i)


#Exemplo 7
# Entrada de Dados:
num = int(input("Digite um número para o cálculo de sua tabuada: "))
print(f"\nCalculando a tabuada do {num}: \n")
for i in range (1,11):
    print(f" {num} x {i} = {num*i}")

#Exemplo 8
while True:
   print("Estou preso dentro de um loop.")


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

#Exemplo 010
notas = [6,7,5,8,9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print(f"Media: {soma/x}")


#Exemplo 011
notas = [0,0,0,0,0]
soma = 0
x = 0
while x < 5:
    notas[x]=float(input(f"Nota {x}:"))
    soma += notas[x]
    x+=1
x = 0
while x < 5:
    print(f"Nota {x}: {notas[x]}")
    x += 1
print(f"Media: {soma/x}")


#exemplo 12
nuber = [111, 7, 2, 1]
print(number[-1])
print(number[-2])

#exemplo 13
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

#exemplo 14
list = [5,3,1,2,4]
print(list)
print()
list.reverse()
print(list) # outputs: [4,0,1,3,5]


#exemplo 15 
list_1 = [5,3,1,2,4]
list_2 = list_1
print("lista 1")
print(list_1)
print()
print("lista 2")
print(list_2)
print()
list_1[2] = 99
print()
print("lista 1")
print(list_1)
print()
print("lista 2")
print(list_2)
print()


#exemplo 16
list_1 = [5,3,99,2,4]
list_2 = list_1[:]
print("lista 1")
print(list_1)
print()
print("lista 2")
print(list_2)
print()
list_1[2] = 99
print()
print("lista 1")
print(list_1)
print()
print("lista 2")
print(list_2)
print()

