sequencia_de_senhas = input().split(",")
aprovadas = []

for i in range(len(sequencia_de_senhas)):

    senha = sequencia_de_senhas[i]
    cond1, cond2, cond3, cond4, cond5= False, False, False, False, False
    for c in senha:
        if c.isalpha() and c.islower():
            cond1= True
        if c.isnumeric():
            cond2= True
        if c.isalpha() and c.isupper():
            cond3= True
        if len(senha) >= 6:
            cond4 = True
        if len(senha) <=12:
            cond5 = True
    
    print(cond1, cond2, cond3, cond4, cond5)
    if cond1 and cond2 and cond3 and cond4 and cond5:
        aprovadas.append(senha)


print(*aprovadas)



