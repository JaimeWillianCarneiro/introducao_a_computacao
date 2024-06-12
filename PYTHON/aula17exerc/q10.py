# finalizado
palavras = ["gato", "cachorro", "coelho"]

tamanho_palavras = {i:len(i) for i in palavras}
print(tamanho_palavras)


maior_tamanho = 0
for word in palavras:
    if len(word) >= maior_tamanho:
        maior_tamanho= len(word)

def alinhar_direita(palavras:list):
    for eacho  in range(len(palavras)):
        tam = tamanho_palavras[palavras[eacho]]
        adiciona = maior_tamanho - tam
        novaPalavra = " "*adiciona + palavras[eacho]
        palavras[eacho] = novaPalavra
        
        print(palavras[eacho])
                
    
alinhar_direita(palavras)
#     gato
# cachorro
#   coelho