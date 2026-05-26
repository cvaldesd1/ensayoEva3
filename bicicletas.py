print("Bienvenido al sistema de gestión de archivos")
capacidad_maima = 25
bicis_disponibles = 25
viajes_activos = 0
ejecutando = True
#ciclo principal
while ejecutando:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Bicicletas disponibles")
    print("2. Arrendar bicicletas (Salida)")
    print("3. Devolver bicicletas (Entrada)")
    print("4. Historial de viajes activos")
    print("5. Salir")
    try:
        opcion = int(input("Selecciona una opción (1-5): "))
        except ValueError
        print("Opción no valida, por favor ingrese un número entre 1 y 5")
        continue
    #opción 1 Bicis disponibles
    if opcion == 1:
        print(f"\n[INFO] cantidad de bicicletas disponibles: {bicis_disponibles}")
    #opción 2 Arrendar bicicletas
    elif opcion == 2:
        print(f"\n--- Arrendar bicicletas (Disponibles: {bicis_disponibles})---")
        if bicis_disponibles == 0:
            print("Lo sentimos, no quedan bicis disponibles")
        else:
            try:
                cantidad_a_arrendar = int(input("¿Cuantas bicis desea arrendar?"))
                