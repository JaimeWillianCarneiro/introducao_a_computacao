dicio = {'aipim': 8, 'limão': 5, 'batata': 5, 'alho': 20}
b = {k:v for k,v in dicio.items() if k.startswith("a") }
print(b)