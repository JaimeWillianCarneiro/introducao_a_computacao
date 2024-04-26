# print("oi")
soma =0
# print(type(soma))
while True:
    
    entrada = input("Digite um número inteiro ou (q) para parar: ")
    if entrada.isnumeric() and int(entrada)== float(entrada):
        soma+=int(entrada)
    elif entrada =="q":
        print(f"Soma: {soma}")
        break
