#=====================================,
#FUNCION PARA GRAFICAR,
#=====================================,
def graficar(funcion):

    # Tamaño del plano
    ancho = 61
    alto = 31

    # Crear matriz vacía
    plano = []

    for i in range(alto):

        fila = []

        for j in range(ancho):
            fila.append(" ")

        plano.append(fila)

    # Centro del plano cartesiano
    centro_x = ancho // 2
    centro_y = alto // 2

    # =====================================
    # DIBUJAR EJES
    # =====================================

    # Eje X
    for x in range(ancho):
        plano[centro_y][x] = "-"

    # Eje Y
    for y in range(alto):
        plano[y][centro_x] = "|"

    # Punto central
    plano[centro_y][centro_x] = "+"

    # =====================================
    # GRAFICAR FUNCION
    # =====================================

    x = -10

    while x <= 10:

        try:

            # Evaluar función
            y = funcion(x)

            # Escala para que no se salga
            y = y / 80

            # Convertir coordenadas matemáticas
            # a coordenadas de pantalla
            pantalla_x = int(centro_x + x)
            pantalla_y = int(centro_y - y)

            # Verificar límites
            if 0 <= pantalla_x < ancho and 0 <= pantalla_y < alto:

                plano[pantalla_y][pantalla_x] = "*"

        except:
            pass

        # Avanzar lentamente para más puntos
        x += 0.2

    # =====================================
    # IMPRIMIR GRAFICA
    # =====================================

    print("\n=== GRAFICA ===\n")

    for fila in plano:
        print("".join(fila))