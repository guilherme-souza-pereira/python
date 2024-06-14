'''
numeros = []
num_par = []
soma = 0
qtd_numeros = 0
maior = float('-inf')
menor = float('inf')

while True:
    try:
        num = float(input("Digite um número (ou '30000' para sair): "))
        
        if num == 30000:
            break
        
        numeros.append(num)
        soma += num
        qtd_numeros += 1

        if num % 2 == 0:
            num_par.append(num)
        
        if num > maior:
            maior = num
        
        if num < menor:
            menor = num
        
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")

media = soma / qtd_numeros
media_par = sum(num_par) / len(num_par) if num_par else 0
qtd_impares = qtd_numeros - len(num_par)
porcentagem_impares = (qtd_impares / qtd_numeros) * 100 if qtd_numeros != 0 else 0

print("Soma dos números digitados:", soma)
print("Quantidade de números digitados:", qtd_numeros)
print("Média dos números digitados:", media)
print("Maior número digitado:", maior)
print("Menor número digitado:", menor)
print("Média dos números pares:", media_par)
print("Porcentagem dos números ímpares entre todos os números digitados:", porcentagem_impares, "%")
'''
'''
lista 2,0'''

soma = 0
qtd_numeros = 0
qtd_pares = 0
maior = float('-inf')
menor = float('inf')
qtd_impares = 0

while True:
    entrada = input("Digite um número (ou '30000' para sair): ")
    
    if entrada == '30000':
        break

    if not entrada.isdigit():  # Verifica se a entrada contém apenas dígitos
        print("Entrada inválida. Por favor, insira um número válido.")
        continue  # Retorna ao início do loop

    num = float(entrada)
    
    soma += num
    qtd_numeros += 1

    if num % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1
    
    if num > maior:
        maior = num
    
    if num < menor:
        menor = num

media = soma / qtd_numeros
media_par = soma / qtd_pares if qtd_pares != 0 else 0
porcentagem_impares = (qtd_impares / qtd_numeros) * 100 if qtd_numeros != 0 else 0

print("Soma dos números digitados:", soma)
print("Quantidade de números digitados:", qtd_numeros)
print("Média dos números digitados:", media)
print("Maior número digitado:", maior)
print("Menor número digitado:", menor)
print("Média dos números pares:", media_par)
print("Porcentagem dos números ímpares entre todos os números digitados:", porcentagem_impares, "%")
