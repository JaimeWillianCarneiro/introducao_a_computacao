def sentido_horizontal():
    matriz = [[i for i in range(5*j+1, 5*j+6)] for j in range(5)]

    return matriz


def sentido_vertical():
    matriz = [[j + i*5 for i in range(5)] for j in range(1, 6)]

    return matriz

def zigue_zague():
    
print(sentido_horizontal())
print(sentido_vertical())