print("1: somar dois numes ")
print("2: raiz quadrada de um numero")
print("digite a opiçao desejada")

escolha = int(input('escolha:'))

if escolha == 1:
    n1 = float(input('numero 1:'))
    n2 = float(input('numero 2:'))
    soma = n1 + n2
    print (soma)
elif escolha == 2:
    n1 = float(input('numero:'))
    raiz = n1/2  
    print (raiz) 
else:
    print("escolha 1 ou 2 ")     



    
