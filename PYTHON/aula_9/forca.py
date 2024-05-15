import random
palavras = ["Borboleta", "Oceano",   "Biblioteca", "Girassol", "Coruja", "Chocolate", "Avental",  "Farol", "Diamante", "Cavaleiro"]

n_tentativas = 0
n_tentativas_max = 5
teste =random.choice(palavras).upper()
# print(teste)

def chose_word(palavras: list) -> str:

    return random.choice(palavras).lower()


def mostra_word(word, caracteres_usados):
    word_to_user = ''
    for c in word:
        if c in caracteres_usados:
            word_to_user += c
        else:
            word_to_user+="_"

    print(f"Palavra:{word_to_user}")


def print_estado_atual(palavra, caracteres_usados, num_tentaiva, num_tentativas_max):
    mostra_word(palavra, caracteres_usados)
    print(f"Letras já utilizadas: {caracteres_usados} ")
    print(f"Numero de tentativas restantes: {num_tentativas_max-num_tentaiva}")
    print()
    

palavra = chose_word(palavras)
caracteres_usados = set()

mostra_word(palavra, caracteres_usados)
c = input("Selecione uma letra: ")
caracteres_usados.add(c)
mostra_word(palavra, caracteres_usados)

while n_tentativas < n_tentativas_max:
    mostra_word(palavra, caracteres_usados)

    c= input("Selecione uma letra")

