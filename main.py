from ManejadorTablasClase import ManejadorTablas
def main():

    print("Bienvenido al manejador de Tablas de Clases")

    manejador = ManejadorTablas()

    while True:
        opcion = input("Por favor, elija una opción: 'CLASS' 'DESCRIBIR' 'SALIR'\n")
        opcion = opcion.split(" ")
        if opcion[0] == "CLASS":
            manejador.definir(opcion[1:])
        elif opcion[0] == "DESCRIBIR":
            print(manejador.describir(opcion[1]))
        elif opcion[0] == "SALIR":
            break
        else:
            print("Opción inválida.")

main()