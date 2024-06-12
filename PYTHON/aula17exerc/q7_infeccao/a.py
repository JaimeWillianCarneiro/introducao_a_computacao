m = 5
n = 5
polos_de_infeccao = [(2, 2, 1), (4, 4, 2)]


def distancia(pontoA, pontoB):
    xA, yA = pontoA[0], pontoA[1]
    xB, yB = pontoB[0], pontoB[1]
    
    distancia = ((xA-xB)**2 + (yA-yB)**2)**(1/2)
    return distancia


def propagar_infeccao(linhas, colunas, polos)-> list:
    matriz = [[0]*colunas]*linhas
    
    for polo in polos:
        coordX = polo[0]
        coordY = polo[1]
        raio = polo[2]
        
        matriz[coordY][coordX] = 1
        
        
        # Analisar a linha atual e as r linhas acima e r linhas 
        #  Abaixo. Sendo assim iriamos analisar (2r+1)*(2r+1)-1 casas
        
        #  Analisando a direita
        
    pass
resultado = propagar_infeccao(m, n, polos_de_infeccao)
print(resultado)
# 0 0 0 0 0
# 0 1 1 1 0
# 0 1 1 1 0
# 0 1 1 1 1
# 0 0 1 1 1