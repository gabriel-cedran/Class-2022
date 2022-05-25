n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

aux1 = n1
aux2 = n2

if n1 >= n2:
    while n2 > 0:
        val1 = n1%10
        val2 = n2%10
        s = val1-val2

        if s != 0:
            print(f"O valor {aux1} não termina em {aux2}")
            break
        else:
            n1 //= 10
            n2 //= 10

    if n2 == 0:
        print(f"O valor {aux1} termina em {aux2}")
    else:
        print(f"O valor {aux1} não termina em {aux2}")