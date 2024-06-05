"""Jogo da forca em Python"""

import random # Modulo utilizado para sortear a palavra a ser descoberta

# Lista de palavras do acervo
palavras = ["Borboleta", "Oceano",   "Biblioteca", "Girassol", "Coruja", "Chocolate", "Avental",  "Farol", "Diamante", "Cavaleiro"]

n_erros = 0 # Numero de erros atual
n_erros_max = 5 # Numero máximo de erros que  o usuario pode cometer



def chose_word(palavras: list) -> str:
    """Escolher Aleatoriamente uma palavra para ser a descoberta no jogo

    Args:
        palavras (list): lista de palavras do acervo

    Returns:
        str: palavra sorteada
    """
    return random.choice(palavras).lower()


def mostra_word(word: str, caracteres_usados: str) -> None:
    """Mostrar situação atual da palavra

    Args:
        word (str): 
        caracteres_usados (str): _description_
    """
    word_to_user = ''
    for c in word:
        if c in caracteres_usados:
            word_to_user += c
        else:
            word_to_user+="_"

    print(f"Palavra: {word_to_user}")


def print_estado_atual(palavra: str, caracteres_usados: list, num_tentaiva: int, num_tentativas_max: int) -> None:
    """_summary_

    Args:
        palavra (str): Palavra a ser descoberta 
        caracteres_usados (list): caracteres já informados pelo usuário
        num_tentaiva (int): numero tentativas atual do usuario
        num_tentativas_max (int): numero limite de tenativas
    """
    mostra_word(palavra, caracteres_usados)
    print(f"Letras já utilizadas: {caracteres_usados} ")
    print(f"Numero de tentativas restantes: {num_tentativas_max-num_tentaiva}")
    print()


def print_win_state():
    print("Você ganhou!")
    exit()

def print_lost_state(word):
    print("Você perdeu!")
    print(f"A Palavra era: {word}")


palavra = chose_word(palavras)
caracteres_usados = set()

mostra_word(palavra, caracteres_usados)
c = input("Selecione uma letra: ").lower()
caracteres_usados.add(c)
mostra_word(palavra, caracteres_usados)

while n_erros < n_erros_max:

    print_estado_atual(palavra, caracteres_usados, n_erros, n_erros_max)
    mostra_word(palavra, caracteres_usados)

    c= input("Selecione uma letra:")
    print()
    if c not in  palavra:
        n_erros+=1
    caracteres_usados.add(c)


    if set(palavra).issubset(caracteres_usados):
        print_win_state()

    elif n_erros == n_erros_max:
        print_lost_state(palavra)
