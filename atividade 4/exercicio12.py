fun_cod = int(input("coloque seu codigo:"))
if fun_cod == 1:
    salario = float(input('seu salario:'))
    aumento = salario*50/100
    print (f"escrituario tem o salario de {aumento+salario}")
elif fun_cod ==2:
    salario = float(input('seu salario:'))
    aumento = salario*35/100
    print (f"secretario o tem o salario de {aumento+salario}")
elif fun_cod ==3:
    salario = float(input('seu salario:'))
    aumento = salario*20/100
    print (f"caixa tem o salario de {aumento+salario}")
elif fun_cod ==4:
    salario = float(input('seu salario:'))
    aumento = salario*10/100
    print (f"gerente tem o salario de {aumento+salario}")
elif fun_cod ==5:
    salario = float(input('seu salario:'))
    print (f"diretor não tem aumento de salario:{salario}")
else:
    print("codido invalido")