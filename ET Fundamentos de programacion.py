import random
import csv
import math

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", 
                "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

sueldos = []

def asignar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos asignados exitosamente.\n")

def clasificar_sueldos():
    menores_800k = []
    entre_800k_y_2M = []
    mayores_2M = []
    total_sueldos = 0

    for i in range(len(trabajadores)):
        if sueldos[i] < 800000:
            menores_800k.append((trabajadores[i], sueldos[i]))
        elif sueldos[i] <= 2000000:
            entre_800k_y_2M.append((trabajadores[i], sueldos[i]))
        else:
            mayores_2M.append((trabajadores[i], sueldos[i]))
        total_sueldos += sueldos[i]

    print("Sueldos menores a $800.000")
    for empleado, sueldo in menores_800k:
        print(f"{empleado}: ${sueldo}")
    print(f"TOTAL: {len(menores_800k)}\n")

    print("Sueldos entre $800.000 y $2.000.000")
    for empleado, sueldo in entre_800k_y_2M:
        print(f"{empleado}: ${sueldo}")
    print(f"TOTAL: {len(entre_800k_y_2M)}\n")

    print("Sueldos superiores a $2.000.000")
    for empleado, sueldo in mayores_2M:
        print(f"{empleado}: ${sueldo}")
    print(f"TOTAL: {len(mayores_2M)}\n")

    print(f"TOTAL SUELDOS: ${total_sueldos}\n")

def ver_estadisticas():
    if not sueldos:
        print("Primero debe asignar los sueldos.\n")
        return

    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)
    promedio_sueldo = sum(sueldos) / len(sueldos)
    media_geometrica = math.prod(sueldos) ** (1 / len(sueldos))

    print(f"Sueldo más alto: ${max_sueldo}")
    print(f"Sueldo más bajo: ${min_sueldo}")
    print(f"Promedio de sueldos: ${promedio_sueldo:.2f}")
    print(f"Media geométrica: ${media_geometrica:.2f}\n")

def reporte_sueldos():
    if not sueldos:
        print("Primero debe asignar los sueldos.\n")
        return

    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])

        for i in range(len(trabajadores)):
            sueldo_base = sueldos[i]
            descuento_salud = sueldo_base * 0.07
            descuento_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - descuento_salud - descuento_afp

            writer.writerow([trabajadores[i], f"${sueldo_base}", f"${descuento_salud:.2f}", f"${descuento_afp:.2f}", f"${sueldo_liquido:.2f}"])

    print("Reporte de sueldos generado exitosamente en 'reporte_sueldos.csv'.\n")

def salir_programa():
    print("Gracias por usar la aplicación. Desarrollado por [Tu Nombre].")
    exit()

def mostrar_menu():
    while True:
        print("Menú de opciones:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            asignar_sueldos()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            salir_programa()
        else:
            print("Opción no válida, por favor intente de nuevo.\n")

if __name__ == "__main__":
    mostrar_menu()
