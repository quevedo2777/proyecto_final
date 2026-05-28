def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def raiz_cuadrada(n,t=0.000001):
    if n < 0:
        return "Error: No se puede calcular la raíz de un número negativo"

    if n == 0:
        return 0.0

    aproximacion = n / 2.0
    
    while True:

        siguiente_aproximacion = 0.5 * (aproximacion + n / aproximacion)# formula de newton raphson para calcular raices
        
        diferencia = aproximacion - siguiente_aproximacion
        if diferencia < 0:
            diferencia = -diferencia

        if diferencia < t:
            return siguiente_aproximacion
        aproximacion = siguiente_aproximacion
from funciones_basicas import potencia
def exp(n,t=7):
    suma=0
    for i in range(t):
        termino=(potencia(n,i))/(factorial(i))#esta ecuacion genera polinimos que sumados da una aproximacion a la funcion exponencial
        suma+=termino#el resultado se acumula en esta variable
    return suma

def sen(n,t=7):
    suma=0
    for i in range(t):
        signo=potencia(-1,i)#calcular variables
        exponente=2*i+1#solo exponentes impares
        termino = (signo * potencia(n, exponente)) / factorial(exponente)#aplicar formula para seno de la serie de taylor
        suma += termino
    return suma

def cos(n,t=7):
    suma=0
    for i in range(t):
        signo=potencia(-1,i)#calcular variables
        exponente=2*i#solo exponentes pares
        termino = (signo * potencia(n, exponente)) / factorial(exponente)#aplicar formula para coseno de la serie de taylor
        suma += termino
    return suma

def ln(n,t=7):
    if n <= 0:
        return "Error: El logaritmo natural solo está definido para números mayores a 0"
    valor_transformado = (n - 1) / (n + 1)
    suma = 0
    for i in range(t):
        exponente = 2 * i + 1#solo exponentes imapres
        termino = potencia(valor_transformado, exponente) / exponente #a diferencia de las anteriores formulas este se divide directamente con el exponente
        suma += termino
        
    return 2 * suma

funciones = {
"lineal": lambda x: 2*x + 1,
"cuadratica": lambda x: x*x,
"cubica": lambda x: x*x*x
}

def evaluar_funciones(coeficientes:list,x:float):
    resultado=0
    for i in range(len(coeficientes)):
        resultado+=potencia(x,i)*coeficientes[i]
    return resultado

def evaluar_funcion_menu(opcion_funcion: str, x: float, funciones: dict):
    if opcion_funcion in funciones:
        funcion_elegida = funciones[opcion_funcion]
        return funcion_elegida(x)
    else:
        return "Error: Opción de función no válida"
