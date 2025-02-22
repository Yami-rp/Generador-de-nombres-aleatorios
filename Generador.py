import random

# Listas predefinidas de nombres y apellidos
nombres = ["Carlos", "Lucía", "Martín", "Sofía", "Fernando", "Valeria", "Javier", "Mariana"]
apellidos = ["Gómez", "Fernández", "López", "Martínez", "Pérez", "Sánchez", "Rodríguez", "Torres"]

def agregar_nombre():
    nuevo_nombre = input("Ingrese un nuevo nombre (o presione Enter para omitir): ").strip()
    if nuevo_nombre:
        nombres.append(nuevo_nombre)
        print(f"Nombre '{nuevo_nombre}' agregado correctamente.")

def agregar_apellido():
    nuevo_apellido = input("Ingrese un nuevo apellido (o presione Enter para omitir): ").strip()
    if nuevo_apellido:
        apellidos.append(nuevo_apellido)
        print(f"Apellido '{nuevo_apellido}' agregado correctamente.")

def generar_nombre():
    return f"{random.choice(nombres)} {random.choice(apellidos)}"

def generar_multiples_nombres(cantidad):
    return [generar_nombre() for _ in range(cantidad)]

# Menú interactivo
while True:
    print("\n--- Generador de Nombres Aleatorios ---")
    print("1. Agregar un nombre personalizado")
    print("2. Agregar un apellido personalizado")
    print("3. Generar un nombre aleatorio")
    print("4. Generar múltiples nombres aleatorios")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_nombre()
    elif opcion == "2":
        agregar_apellido()
    elif opcion == "3":
        print("\nNombre generado:", generar_nombre())
    elif opcion == "4":
        cantidad = int(input("¿Cuántos nombres desea generar? "))
        print("\nNombres generados:")
        for nombre in generar_multiples_nombres(cantidad):
            print("-", nombre)
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
