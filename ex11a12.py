#cria lista mês
Mmes=["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

#Cria matriz
m = [0]*4

for i in range(4):
    m[i] = [0]*12
    for j in range(12):
        m[i][j] = int(input())

#Variaveis
TotalAnual = 0
MaiorGeral = 0

#Verificação celula por celula
for j in range(12):
    TotalMes = 0
    for i in range(4):
        TotalMes += m[i][j]
        if m[i][j] > MaiorGeral:
            #Guarda o maior valor do mês
            MaiorGeral = m[i][j]
            Mes = j
            Semana = i

    #Soma os meses para gerar o valor do ano
    TotalAnual += TotalMes
    
    #Printa o valor e a string da matriz mês // Printa a produção anual e semanal e printa o nome do mês 
    print("Total de peças em", Mmes[j], "=", TotalMes)
    print("Produção anual =", TotalAnual)
    print("Maior produção semanal foi de:", MaiorGeral, "Ocorreu na", Semana, "a. semana do mês:", Mmes[m])