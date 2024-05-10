def calculadora(num1: float, num2: float, oper: str):
    def soma():
        return num1 +num2
    def multiplicao():
        return num2*num1
    def divisao():
        return num1/num2
    def subtracao():
        return num1 -num2
    
    if oper.lower() == "soma":
        return soma()
    elif oper.lower() =="subtracao":
        return subtracao()
    elif oper.lower() == "multiplicacao":
        return multiplicao()
    else: return divisao()

print(calculadora(1, 2, "soma"))

print(calculadora(1, 2, "multiplicacao"))
print(calculadora(1, 2, "divisao"))
print(calculadora(1, 2, "subtracao"))