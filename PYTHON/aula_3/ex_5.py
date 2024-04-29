titulo = "Brilho Eterno de Uma Mente Sem Lembranças"
print(f"Tamanho da lista: {len(titulo)}")
print(f"String em maiúsculo: {titulo.upper()}")
print(f"String em minúsculo: {titulo.lower()}")
print(f"Numero de vezes que aparece o 'a' na string: {titulo.count('a')}")

primeiro_nome = "Jaime"
ultimo_nome = "Silva"

nome_completo = primeiro_nome + " " +  ultimo_nome
print(nome_completo)

nome, sobrenome = nome_completo.split()
print(nome)
print(sobrenome)
nomeCompleto = nome + " " + sobrenome


frase = "I love python"
lista = frase.split()
print(lista)
pos = lista.index("python")
lista[pos] = "java"
new_frase = " ".join(lista)

print(new_frase)
