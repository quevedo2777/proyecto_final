#funciones basicas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre cero"

def potencia(base, exponente):

    resultado = 1

    for i in range(exponente):
        resultado = resultado * base

    return resultado