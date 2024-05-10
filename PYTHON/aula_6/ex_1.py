def calcular_total_compras(valor: float):
    

    if  500 <= valor <1000:
         valor = valor*0.9
    elif 1000 <= valor < 1500:
         valor = valor*0.8
    elif 1500 <= valor:
         valor = 0.3*valor
    

    print(f"Valor a ser pago: R$ {valor}")



while True:
     valor = float(input("Digite o valor total das compras: (ou digite '0' para sair) "))
     if valor==0:
          print("Programa finalizado!")
          break
          
     else:
          calcular_total_compras(float(valor))


