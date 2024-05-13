"""
Inverter lista
"""
def inverter_lista(lista: list):
    if len(lista)==1:
        return lista
    return [lista[-1]] + inverter_lista(lista[:-1])

lista = [1, 2, 3,4,5]
print(inverter_lista(lista))
# 5, 4, 3, 2, 1