print("Bienvenido a su programa de validación de datos")
estudiantes = {}

def registrar_estudiante():
    try:
        nombre = input("Ingrese el nombre del estudiante: ")
        identificacion = input("Ingrese el número de identificación: ")

        if identificacion in estudiantes:
            print("Ya existe un estudiante con esa identificación.")
            return

        edad = int(input("Ingrese la edad del estudiante: "))
        notas = []

        print("Ingrese al menos 3 notas:")
        while len(notas) < 3:
            try:
                nota = float(input(f"Ingrese nota {len(notas) + 1}: "))
                if 0 <= nota <= 5:
                    notas.append(nota)
                else:
                    print("La nota debe estar entre 0 y 5.")
            except ValueError:
                print("Debe ingresar un número válido.")

        estudiantes[identificacion] = {
            "nombre": nombre,
            "edad": edad,
            "notas": notas
        }
        print("Estudiante registrado con éxito.")
    except Exception as e:
        print(f" Error al registrar estudiante: {e}")

def consultar_estudiante():
    identificacion = input("Ingrese la identificación del estudiante: ")
    estudiante = estudiantes.get(identificacion)

    if estudiante:
        print(f"\nNombre: {estudiante['nombre']}")
        print(f" Edad: {estudiante['edad']}")
        print(f" Notas: {estudiante['notas']}")
        promedio = sum(estudiante['notas']) / len(estudiante['notas'])
        print(f"Promedio: {promedio:.2f}\n")
    else:
        print("Estudiante no encontrado.")

def actualizar_notas():
    identificacion = input("Ingrese la identificación del estudiante: ")
    estudiante = estudiantes.get(identificacion)

    if estudiante:
        nuevas_notas = []
        print("Ingrese las nuevas notas (mínimo 3):")
        while len(nuevas_notas) < 3:
            try:
                nota = float(input(f"Nota {len(nuevas_notas) + 1}: "))
                if 0 <= nota <= 5:
                    nuevas_notas.append(nota)
                else:
                    print("La nota debe estar entre 0 y 5.")
            except ValueError:
                print("Ingrese una nota válida.")
        estudiante["notas"] = nuevas_notas
        print("Notas actualizadas correctamente.")
    else:
        print("Estudiante no encontrado.")

def eliminar_estudiante():
    identificacion = input("Ingrese la identificación del estudiante: ")
    if identificacion in estudiantes:
        del estudiantes[identificacion]
        print("Estudiante eliminado correctamente.")
    else:
        print("Estudiante no encontrado.")

def ver_todos_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    print("\n Listado General de Estudiantes:")
    for id, info in estudiantes.items():
        promedio = sum(info['notas']) / len(info['notas'])
        print(f"{id} | Nombre: {info['nombre']} | Edad: {info['edad']} | Promedio: {promedio:.2f}")
    print()

def menu():
    while True:
        print("\n=== Menú de Opciones ===")
        print("1. Registrar estudiante")
        print("2. Consultar estudiante")
        print("3. Actualizar notas")
        print("4. Eliminar estudiante")
        print("5. Ver todos los estudiantes")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            consultar_estudiante()
        elif opcion == "3":
            actualizar_notas()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            ver_todos_estudiantes()
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu()






