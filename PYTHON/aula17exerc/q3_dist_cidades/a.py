# Dicionário de coordenadas das pessoas
pessoas = {'Alice': (1, 2), 'Bob': (3, 4), 'Charlie': (6, 8), 'David': (10, 10)}

# Dicionário de coordenadas das cidades
cidades = {'A': (2, 3), 'B': (5, 5), 'C': (9, 9)}

def cidade_mais_proxima(pessoas: dict, cidades: dict) -> dict:
    cidade_mais_proxima = {pessoa: "" for pessoa in pessoas.keys()}
    for pessoa, local in pessoas.items():
        menorDistancia = 1000
        cidadeMaisPerto = ""
        for cidade, coord in cidades.items():
            distancia = ((local[0]-coord[0])**2 + (local[1]-coord[1])**2)**(1/2)
            if distancia<menorDistancia:
                menorDistancia= distancia
                cidadeMaisPerto = cidade
        cidade_mais_proxima[pessoa]= cidadeMaisPerto
    
    return cidade_mais_proxima
     
#Chamada da função
cidades_proximas = cidade_mais_proxima(pessoas, cidades)

# Saída esperada
print(cidades_proximas)  # Deve retornar {'Alice': 'A', 'Bob': 'A', 'Charlie': 'C', 'David': 'C'}