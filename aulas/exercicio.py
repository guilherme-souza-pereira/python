
Exercicio 3

nota1 = float(input("Digite Nota1: "))
nota2 = float(input("Digite Nota2: "))
nota3 = float(input("Digite Nota3: "))
peso1 = float(input("Digite peso1: "))
peso2 = float(input("Digite peso2: "))
peso3 = float(input("Digite peso3: "))

media = (nota1*peso1+nota2*peso2+nota3*peso3)/(peso1+peso2+peso3)

print("A media ponderada das notas é: ",media)

Exercicio 6
salario_base = float(input("Digite salario base do funcionario: "))

gratificacao = salario_base * 0.05

imposto = salario_base * 0.07

salario_receber = salario_base + gratificacao - imposto

print(f"O salario a receber é:{salario_receber}")

Exercicio 10
import math
raio = float(input('Digite raio:'))

#area = (3.14 * (raio*raio))
#area = 3.14 * (raio**2)
area = math.pi * raio**2

print("A area do Circulo é:",area)
