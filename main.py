
# Se comienza el proyecto ordenando las variables y condicionales

print("Bienvenido al sistema en linea de vestidos de baño")

print("(1)  Inventario")
print("(2)  ventas")
print("(3)  Reportes Generales")
print("(4)  Reclamos")
print("(5) Salir")

opcion_usuario = int(input("Digite la opcion que necesita: "))   # la opcion se escoge de acuerdo al numero que tiene cada menu


if opcion_usuario == 1:
    print("Bienvenido al inventario: ")

    print("(1)  Agregar productos")
    print("(2)  Modificar productos")
    print("(3)  Eliminar producto")
    print("(4) consultas de inventario")
    print("(5)  Devolverse al menu principal")  # para poder controlar como volver al menu principal se piensa usar funciones

    opcion_usuario2 = int(input("Digite la opcion que necesita: "))  # para trabajar con el almacenamiento de los productos se usaran diccionarios

    if opcion_usuario2 == 1:
        print("Trabajo en progreso... ")

    elif opcion_usuario2 == 2:
        print("Trabajo en progreso... ")

    elif opcion_usuario2 == 3:
        print("Trabajo en progreso...")

    elif opcion_usuario2 == 4:
        print("Trabajo en progreso...")

    elif opcion_usuario2 == 5:
        print("Saliendo del programa...")


elif opcion_usuario == 2:
    print("Bienvenido al menu de ventas: ")

    print("(1)  Mostrar productos disponibles: ")
    print("(2)  Realizar la venta: ")
    print("(3)  Generar factura final ")
    print("(4)  Devolverse al menu principal:")

    opcion_usuario2 = int(input("Digite la opcion que necesita: "))

    if opcion_usuario2 == 1:
        print("Trabajo en progreso... ")

    elif opcion_usuario2 == 2:
        print("Trabajo en progreso... ")

    elif opcion_usuario2 == 3:
        print("Trabajo en progreso...")   # para almacenar datos de clientes y productos se piensan usar diccionarios y listas

    elif opcion_usuario2 == 4:
        print("saliendo del programa...")


elif opcion_usuario == 3:
    print("Trabajo en progreso: ")   # de momento se deja sin hacer nada porque se piensa generar un archivo txt con la informacion pedida


elif opcion_usuario == 4:
    nombre_usuario = input("Estimado usuario, digite su nombre para proceder ")

    cantidad_reclamos = int(input("Cuantos reclamos deseas ingresar? "))

    for i in range(cantidad_reclamos):
        pass   # Aqui se almacenaran los reclamos en una lista para despues guardarse en un archivo txt

    print("Trabajo en progreso...")


elif opcion_usuario == 5:
    print("Saliendo del programa, !Gracias por preferirnos¡ ... ")








