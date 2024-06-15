
def x_venceu(matriz):
    coluna1 = [ matriz[i][0] for i in range(3)  ]
    coluna2 = [ matriz[i][1] for i in range(3)  ]
    coluna3 = [ matriz[i][2] for i in range(3)  ]
    diagonal1 = [matriz[i][i] for i in range(3)]
    diagonal2 = [matriz[i][i] for i in range(2, -1, -1)]
    
    if matriz[0].count("X")==3 or matriz[1].count("X")==3 or matriz[2].count("X")==3:
        return True
    

    elif coluna1.count("X") ==3 or  coluna2.count("X") ==3 or  coluna3.count("X") ==3:
        return True

    elif diagonal1.count("X") ==3 or diagonal2.count("X") ==3:
        return True
    else:
        return False

def o_venceu(matriz):
    coluna1 = [ matriz[i][0] for i in range(3)  ]
    coluna2 = [ matriz[i][1] for i in range(3)  ]
    coluna3 = [ matriz[i][2] for i in range(3)  ]
    diagonal1 = [matriz[i][i] for i in range(3)]
    diagonal2 = [matriz[i][i] for i in range(2, -1, -1)]
    
    if matriz[0].count("O")==3 or matriz[1].count("O")==3 or matriz[2].count("O")==3:
        return True
    

    elif coluna1.count("O") ==3 or  coluna2.count("O") ==3 or  coluna3.count("O") ==3:
        return True

    elif diagonal1.count("O") ==3 or diagonal2.count("O") ==3:
        return True
    else:
        return False
  
def resultado(matriz: list) -> None:
   
   if x_venceu(matriz):
       print(0)
   elif o_venceu(matriz):
       print(1)
   else:
       print(-1)
       

tabuleiro = [["O", "X", "O"],["O", "X", "O"],
["X", "O", "X"]]





def verificar_vencedor(tabuleiro):
    # Verifica linhas
    vencedor = False
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2]:
            #complete aqui
            vencedor = linha[0]
            break
    
    # Verifica colunas
    for i in range(3):
        #  complete aqui
        if tabuleiro[0][i] ==  tabuleiro[1][i] ==  tabuleiro[2][i]:
            vencedor =  tabuleiro[0][i]
            break
            #complete aqui
    
    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        vencedor = tabuleiro[0][0]
        #complete aqui
    #complete aqui
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        vencedor =  tabuleiro[0][2]
        #complete aqui
    
    
    if vencedor:
        if vencedor =="X": return 0
        else: return 1
    else: return -1
            
print(verificar_vencedor(tabuleiro))