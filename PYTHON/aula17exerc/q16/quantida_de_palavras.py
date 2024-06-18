arquivo = open('PYTHON/aula17exerc/q16/ari.txt', 'r', encoding='utf-8')

conteudo = arquivo.read()
conteudo = conteudo.lower()
palavras = []
dict_palavras = dict()
pontuacoes=  {'.', ',', '!', '?', ';', ':', '-', '(', ')', '[', ']', '{', '}', '"', "'", '...'}

#  Padronizar as palavras
for palavra in conteudo.split():
    
    for c in palavra:
        if c in pontuacoes:
            palavra.replace(c, ' ')
    palavras.append(palavra)    


total_palavras = len(palavras)

dict_palavras = {palavra: palavras.count(palavra) for palavra in palavras}    
aparicoes = [valor for valor in dict_palavras.values()]

print()
top_5_aparicoes=sorted(aparicoes, reverse=True)[:5]
top_5_palavras= [(palavra,dict_palavras[palavra]) for palavra in dict_palavras.keys() if dict_palavras[palavra] in top_5_aparicoes ]
print("Top 5 palavras no texto")
# print(top_5_palavras)


for i in range(5):
    palavra = top_5_palavras[i][0]
    qntd_aparicoes = top_5_palavras[i][1]
    print(f"{i+1}. {palavra}: {qntd_aparicoes}")


# Analisar sequencias

sequencias = [palavras[each] + " " + palavras[each+1] for each in range(total_palavras-1)]

frequencia_seq = {sequencia: sequencias.count(sequencia) for sequencia in sequencias}
aparicoes_seq = [aparicao for aparicao in frequencia_seq.values()]
top_5_aparicoes_seq = sorted(aparicoes_seq, reverse=True)[:5]

top_5_sequencia = [(sequencia,frequencia_seq[sequencia]) for sequencia in frequencia_seq.keys() if frequencia_seq[sequencia] in top_5_aparicoes_seq ] 

print("Top 5 sequências no texto")


for i in range(5):
    sequencia = top_5_sequencia[i][0]
    qntd_aparicoes = top_5_sequencia[i][1]
    print(f"{i+1}. {sequencia}: {qntd_aparicoes}")

arquivo.close()
