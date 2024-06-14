adicional = 0
tot_imp = 0
qtd_b = 0
qtd_n = 0
qtd_c = 0
for i in range (1,13,1):
preco=float(input("\nDigite o preço do unitário do produto "))
refri=input("Este produto necessita de refrigeração? ")
categ=input("Digite a categoria do produto (A-alimentação, L-limpeza, V-vestuário) ")
if (preco <= 20):
if (categ == 'A'):
custo_est = 2
if (categ == 'L'):
custo_est = 3
if (categ == 'V'):
custo_est = 4
if (preco > 20 and preco <= 50):
if (refri == 'S'):
custo_est = 6
else:
custo_est = 0
if (preco > 50):
if (refri == 'S'):
if (categ == 'A'):
custo_est = 5
if (categ == 'L'):
custo_est = 2
if (categ == 'V'):
custo_est = 4
else:
if (categ == 'A' or categ == 'V'):
custo_est = 0
if (categ == 'L'):
custo_est = 1
if (categ != 'A' and refri != 'S'):
imp = preco * 2 / 100
else:
imp = preco * 4 / 100
preco_final = preco + custo_est + imp
print(f"\nCusto de estocagem = {custo_est}")
print(f"\nValor do imposto = {imp}")
print(f"\nPreço final = {preco_final}")
if (preco_final <= 20): 
qtd_b = qtd_b + 1
print(f"\nClassificação Barato")
if (preco_final > 20 and preco_final <= 100):
qtd_n = qtd_n + 1
print(f"\nClassificação Normal")
if (preco_final > 100):
qtd_c = qtd_c + 1
print(f"\nClassificação Caro")
adicional = adicional + custo_est + imp
tot_imp = tot_imp + imp
if (i == 1):
maior_p = preco_final
menor_p = preco_final
else:
if (preco_final > maior_p):
maior_p = preco_final
if (preco_final < menor_p):
menor_p = preco_final
adicional = adicional / 12
print(f"\nValor adicional = {adicional}")
print(f"\nMaior pre‡o final = {maior_p}")
print(f"\nMenor pre‡o final = {menor_p}")
print(f"\nTotal dos impostos = {tot_imp}")
print(f"\nQuantidade de produtos baratos {qtd_b}")
print(f"\nQuantidade de produtos normais {qtd_n}")
print(f"\nQuantidade de produtos caros {qtd_c}")