# Crear una aplicación para gestionar una lista de contactos
# agregar
# modificar  TAREA
# buscar
# eliminar

# Definir todas las funciones

# Funcion para agregar contactos
def agregar_contacto(lista_contacto, nombre, telefono, correo):
    contacto = (nombre, telefono, correo)
    lista_contacto.append(contacto)
    print(f'Contacto {nombre} agregado exitosamente')

# Funcion para presentar los datos de las listas
def mostrar_contactos(lista_contacto):
    if lista_contacto:
        print("La lista de contactos es: ")
        for contacto in lista_contacto:
            print(f'Nombre: {contacto[0]}, Telefono: {contacto[1]}, correo: {contacto[2]}')
    else:
        print("No hay contactos a presentar")


# Funcion para buscar un contacto
def buscar_contacto(lista_contato, nombre):
    for contacto in lista_contato:
        if contacto[0] == nombre:
            print(f'Nombre: {contacto[0]}, Telefono: {contacto[1]}, correo: {contacto[2]}')
            return contacto
    print(f'Contacto {nombre} no encontrado')
    return None

# Funcion para eliminar un contacto
def eliminar_contacto(lista_contato, nombre):
    for contacto in lista_contato:
        if contacto[0] == nombre:
            lista_contato.remove(contacto)
            print(f'Contacto {nombre} eliminado exitosamente')
            return
    print(f'Contacto {nombre} no encontrado')

# Función para modificar un contacto
def modificar_contacto(lista_contacto, nombre):
    contacto = buscar_contacto(lista_contacto, nombre)
    if contacto:
        nuevo_nombre = input("Ingrese el nuevo nombre (o presione Enter para mantener el actual): ") or contacto[0]
        nuevo_telefono = input("Ingrese el nuevo teléfono (o presione Enter para mantener el actual): ") or contacto[1]
        nuevo_correo = input("Ingrese el nuevo correo (o presione Enter para mantener el actual): ") or contacto[2]
        
        # Actualizar el contacto
        lista_contacto[lista_contacto.index(contacto)] = (nuevo_nombre, nuevo_telefono, nuevo_correo)
        print(f'Contacto {nombre} modificado exitosamente')


# Diccionario para almacenar listas de contactos por categoria
contactos = {
    "personales": [],
    "profesionales": []
}
         
# Menú de opciones para gestionar contactos
def menu():
    while True:
        print("\n--- Menú de Gestión de Contactos ---")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Modificar contacto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            categoria = input("¿Categoría del contacto (personales/profesionales)? ").lower()
            nombre = input("Ingrese un nombre: ")
            telefono = input("Ingrese el teléfono: ")
            correo = input("Ingrese el correo: ")
            agregar_contacto(contactos[categoria], nombre, telefono, correo)

        elif opcion == '2':
            categoria = input("¿Categoría de los contactos a mostrar (personales/profesionales)? ").lower()
            mostrar_contactos(contactos[categoria])

        elif opcion == '3':
            categoria = input("¿Categoría del contacto a buscar (personales/profesionales)? ").lower()
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            buscar_contacto(contactos[categoria], nombre)

        elif opcion == '4':
            categoria = input("¿Categoría del contacto a eliminar (personales/profesionales)? ").lower()
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            eliminar_contacto(contactos[categoria], nombre)

        elif opcion == '5':
            categoria = input("¿Categoría del contacto a modificar (personales/profesionales)? ").lower()
            nombre = input("Ingrese el nombre del contacto a modificar: ")
            modificar_contacto(contactos[categoria], nombre)

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

# Iniciar el menú
menu()