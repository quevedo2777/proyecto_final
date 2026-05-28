# main.py
# Realizar menú y coordinar ejecución de la app
import funciones_basicas
import funciones_cientificas
import graficadora

#inicializamos la estructura global del historial 
historial = []

def mostrar_menu():
    """Imprime las opciones principales de la calculadora en la consola"""
    print("\n=============================================")
    print("    CALCULADORA CIENTÍFICA GRAFICADORA")
    print("=============================================")
    print("1. Menú de operaciones básicas")
    print("2. Menú de operaciones científicas")
    print("3. Evaluar función")
    print("4. Graficar función")
    print("5. Ver historial de operaciones")
    print("6. Fin del programa")
    print("=============================================")

def main():
    opcion = 0
    
    while opcion != 6:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido (1-6).")
            continue
            
        # Opcion 1: Ejecutar función básica
        if opcion == 1:
            print("\n--- MENÚ DE OPERACIONES BÁSICAS ---")
            print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Potencia")
            sub_opc = input("Seleccione operación básica: ")
            
            try:
                if sub_opc in ["1", "2", "3", "4", "5"]:
                    num_a = float(input("Ingrese el primer número: "))
                    num_b = float(input("Ingrese el segundo número: "))
                    
                    if sub_opc == "1":
                        res = funciones_basicas.sumar(num_a, num_b)
                        operacion = f"{num_a} + {num_b}"
                    elif sub_opc == "2":
                        res = funciones_basicas.restar(num_a, num_b)
                        operacion = f"{num_a} - {num_b}"
                    elif sub_opc == "3":
                        res = funciones_basicas.multiplicar(num_a, num_b)
                        operacion = f"{num_a} * {num_b}"
                    elif sub_opc == "4":
                        res = funciones_basicas.dividir(num_a, num_b)
                        operacion = f"{num_a} / {num_b}"
                    elif sub_opc == "5":
                        res = funciones_basicas.potencia(num_a, num_b)
                        operacion = f"{num_a} ^ {num_b}"
                        
                    print(f"Resultado: {res}")
                    historial.append(f"Cálculo Básico: {operacion} -> {res}")
                else:
                    print("Opción de operación básica no válida.")
            except ValueError:
                print("Error: Entrada de datos inválida para la operación.")

        # Opcion 2: Ejecutar función científica
        elif opcion == 2:
            print("\n--- MENÚ DE OPERACIONES CIENTÍFICAS ---")
            print("1. Raíz Cuadrada\n2. Seno\n3. Coseno\n4. Exponencial (e^x)\n5. Logaritmo Natural (ln)\n6. Factorial")
            sub_opc = input("Seleccione operación científica: ")
            
            try:
                # Caso especial para Factorial (requiere un único número entero)
                if sub_opc == "6":
                    num = int(input("Ingrese un número entero no negativo: "))
                    res = funciones_cientificas.factorial(num)
                    print(f"Resultado: {res}")
                    historial.append(f"Factorial de {num} -> {res}")
                
                # Casos para funciones científicas que toman un número flotante
                elif sub_opc in ["1", "2", "3", "4", "5"]:
                    num = float(input("Ingrese el número / argumento: "))
                    
                    if sub_opc == "1":
                        res = funciones_cientificas.raiz_cuadrada(num)
                        historial.append(f"Raíz cuadrada de {num} -> {res}")
                    elif sub_opc == "2":
                        res = funciones_cientificas.sen(num)
                        historial.append(f"Seno({num}) -> {res}")
                    elif sub_opc == "3":
                        res = funciones_cientificas.cos(num)
                        historial.append(f"Coseno({num}) -> {res}")
                    elif sub_opc == "4":
                        res = funciones_cientificas.exp_taylor(num, 15)
                        historial.append(f"Exponencial e^{num} -> {res}")
                    elif sub_opc == "5":
                        res = funciones_cientificas.ln_taylor(num, 20)
                        historial.append(f"Logaritmo Natural ln({num}) -> {res}")
                        
                    print(f"Resultado: {res}")
                else:
                    print("Opción de operación científica no válida.")
            except ValueError:
                print("Error: Debe ingresar un valor numérico válido.")

        # Opcion 3: Ejecutar evaluar funciones
        elif opcion == 3:
            print("\n--- EVALUAR FUNCIÓN ---")
            print("1. Evaluar Función Predefinida (Lineal, Cuadrática, Cúbica, etc.)")
            print("2. Evaluar Polinomio Personalizado (Usa Listas de Coeficientes)")
            tipo = input("Seleccione opción de evaluación: ")
            
            if tipo == "1":
                print("Funciones disponibles: lineal, cuadratica, cubica, seno, coseno, raiz")
                func_nom = input("Escriba el nombre de la función: ").lower()
                val_x = float(input("Ingrese el valor de X: "))
                res = funciones_cientificas.evaluar_funcion_menu(func_nom, val_x, funciones_cientificas.funciones)
                print(f"Resultado f(x): {res}")
                historial.append(f"Evaluación predefinida '{func_nom}' en X={val_x} -> {res}")
                
            elif tipo == "2":
                print("Polinomio: c0 + c1*x + c2*x^2 ...")
                datos = input("Ingrese coeficientes separados por comas (ej. 3,2,5): ")
                lista_coef = [float(c) for c in datos.split(",")]
                val_x = float(input("Ingrese el valor de X: "))
                res = funciones_cientificas.evaluar_funciones(lista_coef, val_x)
                print(f"Resultado del polinomio P(x): {res}")
                historial.append(f"Polinomio {lista_coef} evaluado en X={val_x} -> {res}")

        # Opcion 4: Ejecutar graficar consola
        elif opcion == 4:
         
            print("\n=== GRAFICADORA ===")
            print("Funciones disponibles:")

            # Mostrar funciones del diccionario
            for nombre in funciones_cientificas.funciones:
                print("-", nombre)

            opcion_funcion = input("\nSeleccione una función: ")

              # Verificar si existe
            if opcion_funcion in funciones_cientificas.funciones:

                # Obtener función
                funcion_seleccionada = funciones_cientificas.funciones[opcion_funcion]

                # Graficar
                graficadora.graficar(funcion_seleccionada)

            else:
                print("Función no válida")
            
            historial.append("Se intentó renderizar una gráfica")

        # Opcion 5: Ejecutar historial de funciones
        elif opcion == 5:
            print("\n--- HISTORIAL DE OPERACIONES ---")
            if len(historial) == 0:
                print("El historial está vacío.")
            else:
                for idx, registro in enumerate(historial, 1):
                    print(f"{idx}. {registro}")

        # Opcion 6: Ejecutar salir de app
        elif opcion == 6:
            print("\nFin del programa. ¡Gracias por usar la calculadora!")
            
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()