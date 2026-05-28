import funciones_cientificas
def graficar(funcion):

    # Tamaño del plano
    ancho = 80
    alto = 30

    # Crear matriz vacía
    plano = []

    for i in range(alto):

        fila = []

        for j in range(ancho):
            fila.append(" ")

        plano.append(fila)

    # Centro de la gráfica
    centro_x = ancho // 2
    centro_y = alto // 2

#dibujar ejes

    # Eje X
    for x in range(ancho):
        plano[centro_y][x] = "-"

    # Eje Y
    for y in range(alto):
        plano[y][centro_x] = "|"

    # Centro
    plano[centro_y][centro_x] = "+"

#graficar funcion

    x = -20

    while x <= 20:

        try:

            y = funcion(x)

            # Escalas distintas para que
            # cada función se vea bien

            if funcion == funciones_cientificas.funciones["cubica"]:
                y = y / 120

            elif funcion == funciones_cientificas.funciones["cuadratica"]:
                y = y / 8

            else:
                y = y / 2

            # Coordenadas de pantalla
            pantalla_x = int(centro_x + x)
            pantalla_y = int(centro_y - y)

            # Verificar límites
            if 0 <= pantalla_x < ancho and 0 <= pantalla_y < alto:

                plano[pantalla_y][pantalla_x] = "*"

        except:
            pass

        # Más puntos para suavizar
        x += 0.2

#imprimir grafica

    print("\n=== GRAFICA ===\n")

    for fila in plano:
        print("".join(fila))