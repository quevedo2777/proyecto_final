def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def raiz_cuadrada(n)
def exp_taylor(x,n):
    suma=0
    for i in range(n):
        termino=(x**i)/(factorial(i))#esta ecuacion genera polinimos que sumados da una aproximacion a la funcion exponencial
        suma+=termino#el resultado se acumula en esta variable
    return suma

