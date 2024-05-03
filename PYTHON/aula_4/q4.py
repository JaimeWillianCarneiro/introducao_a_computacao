lista_de_palavras = input("Insira as palavras: ").split(",")
lista_ordenada = sorted(lista_de_palavras)

print(*lista_ordenada, sep=",")


