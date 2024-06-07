
def detectar_colisao(circulo1: tuple,circulo2: tuple) -> str:
    x1, y1 = circulo1[0], circulo1[1]
    x2, y2= circulo2[0], circulo2[1]
    r1, r2 = circulo1[2], circulo2[2]
    dist_centros = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    soma_raios = r1 +r2
    print(dist_centros, soma_raios)
    

    if soma_raios > dist_centros:
        return "Colidem"
    else:
        return "Não colidem"

circulo1 = (1, 1, 2)
circulo2 = (4, 5, 3)
resultado = detectar_colisao(circulo1, circulo2)
print(resultado) # Não colidem

circulo1 = (0, 0, 5)
circulo2 = (3, 4, 2)
resultado = detectar_colisao(circulo1, circulo2)
print(resultado) # Colidem