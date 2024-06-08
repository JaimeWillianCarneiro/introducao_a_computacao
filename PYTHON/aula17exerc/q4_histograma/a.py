""" 
O que fazer:
1. receber a lista de numeros
2. Ordenar a lista de numeros
3. pegar o menor e o maior valor
4. Criar o dicionarios com as keys de intervalo
"""

def freq_intervalos(lista_numeros: list) -> dict:
    """Calcular a frequência de numeros que aparecem 
    em cada um dos 5 intervalos 

    Args:
        lista_numeros (list): _description_

    Returns:
        dict: dicionario em que cada chave é uma string "ini-fim" e
    """

    lista_ordenada = sorted(lista_numeros)
    menor_num = lista_ordenada[0]
    maior_num = lista_ordenada[-1]
    tamanho_intervalo_maior = maior_num-menor_num+1
    tamanho_cada_intervalo = tamanho_intervalo_maior//5

    frequencia_intervalos = dict()

    ini =menor_num
    
    for each in range(5):
        fim = ini + tamanho_cada_intervalo-1
        cont = 0 
        for each_num in lista_numeros:
            if ini <=each_num<= fim:
                cont+=1
          
        chave = f"{ini}-{fim}"

        frequencia_intervalos[chave] = cont
        ini = fim+1
    

    return frequencia_intervalos

lista_numeros = [70, 5, 12, 40, 55, 27, 33, 20, 63, 94, 88, 99]
resultado = freq_intervalos(lista_numeros)
print(resultado)
