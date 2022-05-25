#exercicio xadrez/cavalo

m = [0]*8
for i in range(8):
    m[i] = [0]*8
    
print("Digite a linha onde o cavalo está:")
L=int(input())
print("Digite a coluna que o cavalo está:")
C=int(input())

for i in range(8):
    for j in range(8):
        if ((i==L-2 or i==L+2)and(j==C-1 or j==C+1)) or ((i==L-1 or i==L+2)and(j==C-2 or j==C+2)):
            m[i][j] = 1

print("Matriz cavalo")
for i in range(8):
    print(m[i])
