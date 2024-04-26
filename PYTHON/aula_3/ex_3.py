dias_da_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
print(f"Terceiro elemento: {dias_da_semana[2]}")
tamanho = len(dias_da_semana)

dias_reversos = [ 0]*tamanho

for i in range(6, -1, -1):
    dia= dias_da_semana[i]
    dias_reversos[6-i]= dia
print(dias_reversos)