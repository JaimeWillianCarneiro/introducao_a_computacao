m = 5
n = 5
polos_de_infeccao = [(2, 2, 1), (4, 4, 2)]


def propagar_infeccao(linhas, colunas, polos)-> list:
    matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]
    
    for polo in polos:
        coordX = polo[1]
        coordY = polo[0]
        raio = polo[2]
        
        matriz[coordY][coordX] = 1
        
        linhas_acima =0
        linhas_abaixo =0
        colunas_direita = 0 
        colunas_esquerda = 0 
        
        #  Vendo quantas linhas acimas posso passar
        if coordY - raio <0:
            linhas_acima = coordY
        else:
            linhas_acima = raio
        
        #  vendo colunas a esquerda  q posso infectar
        if coordX - raio <0:
            colunas_esquerda=coordX
        else: colunas_esquerda= raio
        
        #  Vendo quantas linhas abaixo posso infectar
        if coordY+ raio > n-1:
            linhas_abaixo = n-1 - coordY
        else:
            linhas_abaixo= raio
        
        #  Vendo quantas colunas a direiat posso infectar
        if coordX + raio > n-1:
            colunas_direita = n-1 - coordX
        else:
            colunas_direita = raio
            
        
        # Analisar a linha atual e as r linhas acima e r linhas 
        #  Abaixo. Sendo assim iriamos analisar (2r+1)*(2r+1)-1 casas
        

        for linha in range(coordY-linhas_acima, coordY+ linhas_abaixo+1):
            
            for coluna in range(coordX-colunas_esquerda, coordX+colunas_direita+1):
                matriz[linha][coluna]=1
        
    return matriz
     
resultado = propagar_infeccao(m, n, polos_de_infeccao)
for linha in resultado:
    print(*linha)
# 0 0 0 0 0
# 0 1 1 1 0
# 0 1 1 1 0
# 0 1 1 1 1
# 0 0 1 1 1