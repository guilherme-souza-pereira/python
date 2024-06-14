traLA = float(input('nota do laboratorio:'))*2
avaSE = float(input('nota do semestre:'))*3
exaFI = float(input('nota do final:'))*5

soma = (traLA+avaSE+exaFI)/10
if soma <= 5:
    print(f'sua media é E') 
elif soma <= 6:
    print(f'voce tirou D')
elif soma <= 7:
    print(f'sua nota é C')
elif soma <= 8:
    print(f'sua nota é B')
else:
    print(f'sua nota é A')               
    

               