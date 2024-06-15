
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
   print() 
   if x_venceu(matriz):
       print(0)
   elif o_venceu(matriz):
       print(1)
   else:
       print(-1)
       

tabuleiro = [["X", "O", "O"],["O", "X", "O"],
["X", "O", "X"]]


resultado(tabuleiro)