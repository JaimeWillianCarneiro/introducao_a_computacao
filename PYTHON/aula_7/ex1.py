def eh_perfeito(num: int) -> bool:
    divisores = []
    for i in range(1, num+1):
        if num%i==0:
            divisores.append(i)
    if sum(divisores)== 2*num:
        return True
    else:
        return False

qtd_numeros_perfeitos = 0
numeros_perfeitos = []

atual = 1
while qtd_numeros_perfeitos <5:
    

    if qtd_numeros_perfeitos ==5:
        break
    if eh_perfeito(atual):
        numeros_perfeitos.append(atual)
        print(numeros_perfeitos)
        qtd_numeros_perfeitos+=1
    
    atual+=1        
    
print(numeros_perfeitos)

print(eh_perfeito(28))