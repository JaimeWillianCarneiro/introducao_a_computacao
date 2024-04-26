numeros = [1,1]
count =  2

for i in range(2, 20):
    num = numeros[i-1] + numeros[i-2]
    numeros.append(num)
print(*numeros)