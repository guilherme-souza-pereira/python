altura = float(input('sua altura:'))
peso = float(input('seu peso:'))

if altura <= 1.19:
    if peso < 60:
        print("A")
    elif peso <= 90:
        print("D")
    else:
        print("G")
elif altura <= 1.70:
    if peso < 60:
        print("B")
    elif peso <= 90:
        print("E")
    else:
        print("H")
else:
    if peso < 60:
        print("C")
    elif peso <= 90:
        print("F")
    else:
        print("I")
                  
         