salario = int(input('Informe seu salario atual: '))


if salario <= 600:
    auxilio = 150
else:
    auxilio = 100



if salario <= 500:
    acrescimo = 0.05 
    print(f"\nSeu novo salário será de R${salario + auxilio +(salario * acrescimo)}") 
elif salario <= 1200:
    acrescimo = 0.12 
    print(f"\nSeu novo salário será de R${salario + auxilio +(salario * acrescimo)}")
else:
    print(f"\nSeu novo salário será de R${salario + auxilio}") 