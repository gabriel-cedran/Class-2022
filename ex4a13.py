#exercicio xadrez/rainha
#obs: mistura do bispo+torre

m = [0]*8
for i in range(8):
    m[i] = [0]*8

print("Digite a linha onde a rainha está:")
L=int(input())
print("Digite a coluna que a rainha está:")
C=int(input())

for i in range(8):
    for j in range(j):
        if (i==L or j==C or i+j==L+C or i-j==L-C):
            m[i][j] = 1

print("Matriz Rainha:")
for i in range(8):
    print(m[i])