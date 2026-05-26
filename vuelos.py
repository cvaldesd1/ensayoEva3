# --- Programa de Control de Carga "Vuelo Chile" ---

# 1. Solicitar cantidad total de equipajes con validación
while True:
    try:
        total_equipajes = int(input("Ingrese la cantidad de equipajes a registrar: "))
        if total_equipajes <= 0:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
            continue  # Reinicia el ciclo si el número es negativo o cero
        break  # Sale del ciclo si el dato es válido
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

# Variables para el conteo final
cabina = 0
bodega = 0
registrados = 0

# 2. Registro por Equipaje
while registrados < total_equipajes:
    print(f"\n--- Registro del Equipaje N°{registrados + 1} ---")
    
    # Validación del Código de Ticket
    ticket = input("Ingrese Código de Ticket (mínimo 5 caracteres, sin espacios): ")
    if len(ticket) < 5 or " " in ticket:
        print("¡Error! El ticket debe tener al menos 5 caracteres y no contener espacios.")
        continue  # Salta el resto del código y vuelve a pedir el ticket actual

    # Validación del Peso
    while True:
        try:
            peso = int(input(f"Ingrese peso del equipaje {ticket} (kg): "))
            if peso <= 0:
                print("¡Error de pesaje! Ingresa un número entero positivo para el peso.")
                continue
            break # Peso válido, salimos de este bucle interno
        except ValueError:
            print("¡Error de pesaje! Ingresa un número entero positivo para el peso.")

    # 3. Clasificación Automática
    if peso > 10:
        print(f">> Ticket {ticket}: Clasificado como Equipaje de Bodega (Sobrecarga).")
        bodega += 1
    else:
        print(f">> Ticket {ticket}: Clasificado como Equipaje de Cabina (Permitido).")
        cabina += 1
    
    registrados += 1 # Aumentamos el contador para pasar al siguiente equipaje

# 4. Salida Final
print("-" * 50)
print(f"¡El avión transportará {cabina} equipajes en Cabina e {bodega} equipajes en Bodega!")
print("¡Manifiesto de carga listo!")
print("-" * 50)