while True:
    print(f"\n1- Imposto ")
    print(f"\n2- Novo Salário ")
    print(f"\n3- Classificação ")
    print(f"\n4- Finalizar o programa ")
    print(f"\nDigite a opção desejada ")
    op=int(input())
    if (op < 1 or op > 4):
        print(f"\nOpção inválida !")
    else:
        if (op == 1):
            sal=float(input("\nDigite o valor do salário\n"))
            if (sal < 500):
                imp = sal * 5 / 100
            if (sal >= 500 and sal <= 850):
                imp = sal * 10 / 100
            if (sal > 850):
                imp = sal * 15 / 100
            print(f"\nValor do imposto a ser pago = {imp}")
        if (op == 2):
            sal=float(input("\nDigite o valor do salário\n "))
            if (sal > 1500):
                aum = 25
            if (sal >= 750 and sal <= 1500):
                aum = 50
            if (sal >= 450 and sal < 750):
                aum = 75
            if (sal < 450):
                aum = 100
            novo_sal = sal + aum
            print(f"Valor do salário com aumento = {novo_sal}")
        if (op == 3):
            sal=float(input("\nDigite o valor do salário\n "))
            if (sal <= 700):
                print("\nMal Remunerado ")
            else:
                print("\nBem Remunerado ")
        if (op == 4):
            break