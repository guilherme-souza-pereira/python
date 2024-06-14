numeros_pares = 0
numeros_impares = 0
numeros_positivos = 0
numeros_negativos = 0



while True:
    numeros = float(input("numeros:"))
    if numeros % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
        
    if numeros > 0:
        numeros_positivos += 1
    else:
        numeros_negativos += 1
            
    pergunta = input("deseja encerrar o programa?")
    
    if pergunta == "s":
        break
     
print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)
print("Números positivos:", numeros_positivos)
print("Números negativos:", numeros_negativos) 
     
     
         
            
            
            
            


    