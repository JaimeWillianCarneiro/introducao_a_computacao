info_livro = {
    "título": "Vermelho, Branco e Sangue Azul ", 
    "preço": 29.90, 
    "autor": "Casey McQuiston", 
    "ano": 2019
}

print(f'Título do livro: {info_livro['título']}')
info_livro['ano'] = 2023
print(info_livro['ano'])

info_livro.pop('autor')
print(info_livro)