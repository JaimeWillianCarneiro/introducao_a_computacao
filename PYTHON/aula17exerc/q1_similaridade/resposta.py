texto1 ="O gato está no telhado."
texto2 = "O gato dorme no telhado."

pontuacoes=  {'.', ',', '!', '?', ';', ':', '-', '(', ')', '[', ']', '{', '}', '"', "'", '...'}

def padronizacao(entrada: str)-> list:
    elementos =  set()
    for palavra in entrada.split():
        print(palavra)
        elemento = ""
        for c in palavra:
            if c not in pontuacoes:
                elemento+=c.upper()

        elementos.add(elemento)
    
    return elementos

print(padronizacao(texto1))
        