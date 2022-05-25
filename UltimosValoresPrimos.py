n = int(input(""))

primos = []
aux = -1

for i in range(1, n):
    cont = 0

    for j in range(1, i+1):
        if i%j  == 0:
            cont += 1
    
    if cont <= 2:
        primos.append(i)
        aux += 1

print(primos[aux], primos[aux-1])