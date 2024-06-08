def encontrar_colisoes(intervalos: dict)-> list:
    colisoes= []
    
    for index1, elem1 in intervalos.items():
        
        for index2, elem2 in intervalos.items():

            if not index1== index2:
                if (elem1[0] <= elem2[1] and elem1[1] >= elem2[0]) or (elem1[1] <= elem2[0] and elem1[0] >= elem2[1]):
                    col = (index1, index2)
                    col_reverse = (index2, index1)
                    if not col in colisoes and col_reverse not in colisoes:
                        colisoes.append(col)
    

    return colisoes


intervalos = {'A': (1, 5), 'B': (3, 7), 'C': (7, 10), 'D': (15, 18)}
resultado = encontrar_colisoes(intervalos)
print(resultado) # [('A', 'B'), ('B', 'C')]