x, y = map(int, input("Insira o número de linhas e colunas separado por (,): ").split(","))
matriz = [[0 for _ in range(y)] for _ in range(x)]
# matriz = [[0]*y]*x
for linha in range(x):
    for coluna in range(y):
        matriz[linha][coluna] = linha*coluna
print(matriz)
