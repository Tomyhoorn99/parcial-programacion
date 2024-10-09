from funciones import *


def main():
    inventario = []
    while True:
        print("Menú Principal")
        print("1 Cargar pacientes")
        print("2 Mostrar lista de pacientes")
        print("3 Buscar paciente por historia clínica")
        print("4 Ordenar pacientes por historia clínica")
        print("5 Mostrar paciente con más días de internación")
        print("6 Mostrar paciente con menos días de internación")
        print("7 Contar pacientes con más de 5 días de internación")
        print("8 Calcular promedio de días de internación")
        print("9 Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cargar_pacientes(inventario)
        elif opcion == "2":
            mostrar_lista_pacientes(inventario)
        elif opcion == "3":
            buscar_paciente(inventario)
        elif opcion == "4":
            ordenar_pacientes(inventario)
        elif opcion == "5":
            paciente_mas_dias(inventario)
        elif opcion == "6":
            paciente_menos_dias(inventario)
        elif opcion == "7":
            contar_pacientes_mas_de_5_dias(inventario)
        elif opcion == "8":
            promedio_dias_internacion(inventario)
        elif opcion == "9":
            print("sistema finalizado.")
            break
        else:
            print("ERROR, intente de nuevo.")
        

if __name__ == "__main__":
    main()















# def main():
#     inventario = []
#     seguir = "S"
#     while seguir == "S":
#         print("Menú Principal")
#         print("1 Cargar pacientes")
#         print("2 Mostrar lista de pacientes")
#         print("3 Buscar paciente por historia clínica")
#         print("4 Ordenar pacientes por historia clínica")
#         print("5 Mostrar paciente con más días de internación")
#         print("6 Mostrar paciente con menos días de internación")
#         print("7 Contar pacientes con más de 5 días de internación")
#         print("8 Calcular promedio de días de internación")
#         print("9 Salir")
        
#         opcion = input("Seleccione una opción: ")
        
#         if opcion == "1":
#             cargar_pacientes(inventario)
#         elif opcion == "2":
#             mostrar_lista_pacientes(inventario)
#         elif opcion == "3":
#             buscar_paciente(inventario)
#         elif opcion == "4":
#             ordenar_pacientes(inventario)
#         elif opcion == "5":
#             paciente_mas_dias(inventario)
#         elif opcion == "6":
#             paciente_menos_dias(inventario)
#         elif opcion == "7":
#             contar_pacientes_mas_de_5_dias(inventario)
#         elif opcion == "8":
#             promedio_dias_internacion(inventario)
#         elif opcion == "9":
#             print("sistema finalizado.")
#             break
#         else:
#             print("ERROR, intente de nuevo.")
#         seguir = input("¿Desea seguir usando el sistema (S/N)? ").upper()

# if __name__ == "__main__":
#     main()



        # quise hacerlo asi, pero al momento de volver o dejar de ingresar, ya no me dejaba usar las demas opciones.