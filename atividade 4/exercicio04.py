numero01 = float(input('numero 1:'))
numero02 = float(input('numero 2:'))
numero03 = float(input('numero 3:'))
menor = min(numero01,numero02,numero03)
maior = max(numero01,numero02,numero03)
meio = (numero01 + numero02 + numero03)- menor - maior
print(menor,meio,maior)
