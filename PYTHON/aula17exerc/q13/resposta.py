

def valida_codigo(codigo:str)-> bool:
    codigo_verificador = 0
    soma_impares = 0 
    soma_pares = 0 
    for index in range(0, 11, 2):
        soma_impares+=int(codigo[index])
    for index in range(1, 12, 2):
        soma_pares+=int(codigo[index])

    soma_pares*=3
    soma = soma_impares + soma_pares
    
    multiplo = 0
    if soma%10==0:
        multiplo = soma+10
    else:
        resto_por_10 = soma%10
        adicionar = 10 - resto_por_10
        multiplo = soma+adicionar
    
    codigo_verificador = multiplo-soma
    
    print(soma_impares, soma)
    print(codigo_verificador, codigo[-1])
    if codigo_verificador == int(codigo[-1]):
        print("Valido")
    else:
        print("Não valido")


valida_codigo("4006381333931")


    
        
    
       
        