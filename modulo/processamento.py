# processamento.py

def preprocessar_texto(texto):
    # Remover espaços laterais
    texto_processado = texto.strip()

    # Color em caixa-baixa
    texto_processado = texto_processado.lower()

    # Remover números
    texto_processado = ''.join([c for c in texto_processado if not c.isdigit()])

    return texto_processado

pontuacoes = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'