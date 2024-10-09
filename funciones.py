def cargar_pacientes(inventario: list[list]):
    while True:
        cantidad_a_ingresar = input("Cuantos pacientes desea ingresar?: ")
        if cantidad_a_ingresar.isdigit() and 0 < int(cantidad_a_ingresar) < 10:
            cantidad_a_ingresar = int(cantidad_a_ingresar)
            break
        print("Por favor, ingrese un dígito mayor que 0 y menor que 10.")

    for _ in range(cantidad_a_ingresar):
        while True:
            historia_clinica = input("Ingrese el numero de historia clinica: ")
            if historia_clinica.isdigit() and int(historia_clinica) > 0:
                historia_clinica = int(historia_clinica)
                break
            print("La historia clinica debe ser un nUmero mayor que 0.")

        while True:
            nombre = input("Ingrese el nombre del paciente: ")
            if nombre.isalpha():
                break
            print("El nombre debe contener solo letras.")

        while True:
            edad = input("Ingrese la edad del paciente: ")
            if edad.isdigit() and 0 < int(edad) < 130:
                edad = int(edad)
                break
            print("La edad debe ser un número entre 1 y 129.")

        diagnostico = input("Ingrese el diagnóstico del paciente: ")

        while True:
            dias_internacion = input("Ingrese la cantidad de días de internación: ")
            if dias_internacion.isdigit():
                dias_internacion = int(dias_internacion)
                break
            print("Los días de internación deben ser un número entero positivo.")

        inventario.append([historia_clinica, nombre, edad, diagnostico, dias_internacion])


def mostrar_lista_pacientes(inventario: list[list]):
    """
    Muestra la lista de pacientes registrados.

    Si no hay pacientes registrados, muestra un mensaje de error.
    Si hay pacientes registrados, los muestra en formato de tabla
    con sus datos.
    """
    if not inventario:
        print("No hay pacientes registrados.")
    else:
        for paciente in inventario:
            print(f"Historia Clinica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnostico: {paciente[3]}, Días de internacion: {paciente[4]}")


def buscar_paciente(inventario: list[list]):
    """
    Busca un paciente en la lista de pacientes registrados.

    Si no hay pacientes registrados, muestra un mensaje de error.
    Si hay pacientes registrados, pide al usuario que ingrese el número de
    historia clínica del paciente a buscar. Si el paciente existe, muestra
    sus datos en formato de tabla. De lo contrario, muestra un mensaje de
    error.
    """
    if not inventario:
        print("No hay pacientes registrados.")
        return

    historia_clinica = input("Ingrese el numero de historia clinica: ")
    while not historia_clinica.isdigit():
        historia_clinica = input("Ingrese el numero de historia clinica: ")
    historia_clinica = int(historia_clinica)

    encontrado = False
    for paciente in inventario:
        if paciente[0] == historia_clinica:
            print(f"Historia clinica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnostico: {paciente[3]}, Días de internacion: {paciente[4]}")
            encontrado = True
            break
    if not encontrado:
        print(f"No se encontro ningun paciente con la historia clinica {historia_clinica}.")


def ordenar_pacientes(inventario: list[list]):
    """
    Ordena la lista de pacientes por número de historia clínica.

    Si no hay pacientes registrados, muestra un mensaje de error.
    Si hay pacientes registrados, se ordena la lista con el algoritmo
    de burbuja 
    """
    if not inventario:
        print("No hay pacientes registrados.")
    else:
        n = len(inventario)
        for i in range(n):
            for j in range(0, n-i-1):
                if inventario[j][0] > inventario[j+1][0]:
                    inventario[j], inventario[j+1] = inventario[j+1], inventario[j]
        print("Pacientes ordenados por numero de historia clinica")


def paciente_mas_dias(inventario: list[list]):
    """
    Muestra el paciente con más días de internación.

    Si no hay pacientes registrados, muestra un mensaje de error.
    Si hay pacientes registrados, busca el paciente con más días de internación
    y muestra su nombre y cantidad de días.
    """
    if not inventario:
        print("No hay pacientes registrados.")
    else:
        paciente_max_dias = inventario[0]
        for i in range(len(inventario)):
            if inventario[i][4] > paciente_max_dias[4]:
                paciente_max_dias = inventario[i]
        print(f"El paciente con más días de internación es: {paciente_max_dias[1]}, con {paciente_max_dias[4]} días.")

def paciente_menos_dias(inventario: list[list]):
    """
    Muestra el paciente con menos días de internación.

    Si no hay pacientes registrados, muestra un mensaje de error.
    Si hay pacientes registrados, busca el paciente con menos días de internación
    y muestra su nombre y cantidad de días.
    """
    if not inventario:
        print("No hay pacientes registrados.")
    else:
        paciente_min_dias = inventario[0]
        for i in range(len(inventario)):
            if inventario[i][4] < paciente_min_dias[4]:
                paciente_min_dias = inventario[i]
        print(f"El paciente con menos días de internación es: {paciente_min_dias[1]}, con {paciente_min_dias[4]} días.")

def contar_pacientes_mas_de_5_dias(inventario: list[list]):
    """
    Cuenta la cantidad de pacientes que tienen más de 5 días de internación.

    Si no hay pacientes registrados, muestra un mensaje de error.
    Si hay pacientes registrados, busca los pacientes con más de 5 días de internación
    y muestra la cantidad de pacientes que cumplen con esa condición.
    """
    if not inventario:
        print("No hay pacientes registrados.")
    else:
        pacientes_mas_de_5_dias = [paciente for paciente in inventario if paciente[4] > 5]
        print(f"Cantidad de pacientes con más de 5 días de internación: {len(pacientes_mas_de_5_dias)}")


def promedio_dias_internacion(inventario: list[list]):
    """
    Calcula el promedio de días de internación de todos los pacientes
    en el inventario.

    Si no hay pacientes registrados, muestra un mensaje de error.
    Si hay pacientes registrados, suma todos los días de internación
    de los pacientes y divide por la cantidad de pacientes.
    
    """
    if not inventario:
        print("No hay pacientes registrados.")
    else:
        total_dias = 0
        for i in range(len(inventario)):
            total_dias += inventario[i][4]
        promedio = total_dias / len(inventario)
        print(f"El promedio de días de internación es: {promedio}")

