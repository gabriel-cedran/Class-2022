L = []
cont = 0

print("Digite os valores: ")
print("* Digite A para interromper o programa *")

while True:
    n = str(input(""))

    if n == "A":
        break
    
    else:
        cont += 1
        val = 0
        i = 0
        for i in range(cont):
            if len(L) == 0:
                L.append(n)
            elif n >= L[i] and val == 0:
                L.insert(i+1, n)
                val += 1

print(*L)