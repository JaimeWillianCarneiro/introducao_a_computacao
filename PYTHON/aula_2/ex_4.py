n = int(input("Numero de linhas: "))
m = int(input("Numero de colunas: "))

print(f"Coluna com {n} 0's")
for _ in range(n): print("0")

print(f"Linha com {m} 0's")
print("0 "*m)

print(f"Uma matriz de 0's com {n} linhas e {m} colunas.")
for linha in range(n):
    print("0 "*m)
