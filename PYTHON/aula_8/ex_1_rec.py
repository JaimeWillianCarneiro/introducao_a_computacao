"""
Soma dos n primeiros numeros naturais
"""
def soma_naturais(n: int):
    if n==1:
        return 1
    else: 
        return n + soma_naturais(n-1)
print(soma_naturais(5))