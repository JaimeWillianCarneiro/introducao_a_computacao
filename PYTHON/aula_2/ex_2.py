lado1 = float(input("Digite o tamanho do primeiro lado do triâgulo: "))
lado2 = float(input("Digite o tamanho do segundo lado do triâgulo: "))
lado3 = float(input("Digite o tamanho do segundo lado do triâgulo: "))

if lado1== lado2 == lado3:
    print("Equilátero")
elif lado1 != lado2 != lado3:
    print("Escaleno")
else:
    print("Isósceles")

