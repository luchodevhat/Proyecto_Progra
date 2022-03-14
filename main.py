


validacion = True               # esta variable sirve para controlar el menu principal

                # inventario predeterminado
pantalonetas_azules = {"nombre":"Pantalonetas Azules", "precio":12000,"cantidad":10,"codigo":1212}
bikinis_rojos = {"nombre":"Bikinis Rojos", "precio":15000,"cantidad":15,"codigo":2222}
pantalonetas_verdes = {"nombre":"Pantalonetas Verdes", "precio":12000,"cantidad":10,"codigo":1111}


inventario = [pantalonetas_azules, bikinis_rojos, pantalonetas_verdes]   # lista que almacena todos los direccionarios, "productos con sus datos"
cantidad = len(inventario)                    # Esta variable es la cantidad de productos disponibles, se inicializa con la funcion len para medir el inventario


            # inicio del programa

while validacion == True:       # Este while nos permite crear un bucle al menu principal


    print("Bienvenido al sistema en linea de vestidos de baño")

    print("(1)  Inventario")
    print("(2)  ventas")
    print("(3)  Reportes Generales")
    print("(4)  Reclamos")
    print("(5) Salir")

    opcion_usuario = int(input("Digite la opcion que necesita: "))

            # menu de inventario

    if opcion_usuario == 1:
        print("Bienvenido al inventario: ")

        print("(1)  Agregar productos")
        print("(2)  Modificar productos")
        print("(3)  Eliminar producto")
        print("(4) consultas de inventario")
        print("(5)  Devolverse al menu principal")

        opcion_usuario2 = int(input("Digite la opcion que necesita: "))

        if opcion_usuario2 == 1:                                         # Este es el menu de agregar productos
            cantidad = int(input("Cuantos productos desea ingresar: "))

            for i in range(cantidad):               # Aqui se ingresan los datos especificos de cada producto
                producto_agregado = {}

                nombre_producto = input("Ingresa el nombre del producto: ")
                precio_producto = int(input("Ingresa el precio del producto: "))
                cantidad_producto = int(input("Ingresa el cantidad del producto: "))
                codigo_producto = int(input("Ingresa el codigo del producto: "))

                producto_agregado = {'nombre': nombre_producto, "precio":precio_producto, "cantidad": cantidad_producto, "codigo":codigo_producto}

                inventario.append(producto_agregado)   # con la funcion append se agrega el diccionario a la lista del inventario
                print("Productos agregados correctamente al inventario.... ")

                producto_agregado = {}  # el diccionario se limpia, para poder seguir agregando otros productos y que no se colapse de informacion


        elif opcion_usuario2 == 2:                          # Este es el menu de modificar productos
            if cantidad != 0:
                producto_escogido = (input("Que producto deseas escoger? "))

                # print("Los datos de los productos son: ")
                # print(f"(1) Codigo de producto: {codigo_producto} ")
                # print(f"(2) Precio de producto: {precio_producto} ")
                # print(f"(3) La cantidad disponble: {cantidad_producto} ")

                for i in inventario:
                   print(f"Productos disponibles")

                   print(f"Nombre: {i['nombre']}", end=' , ')
                   print(f"Precio: {i['precio']}", end=' , ')
                   print(f"Cantidad: {i['cantidad']}", end=' , ')
                   print(f"Codigo: {i['codigo']}", end=' , ')


                opcion = int(input("Que deseas modificar: "))

                if opcion == 1:                    # menu "modificar el codigo de producto"

                    codigo_producto = int(input("Ingresa nuevamente el codigo del producto "))
                    print(f"Completado, ahora la cantidad es de {codigo_producto}")

                elif opcion == 2:                 # menu "modificar el precio de proucto"

                    precio_producto = int(input("Ingresa nuevamente el precio del producto "))
                    print(f"Completado, ahora la cantidad es de {precio_producto}")


                elif opcion == 3:                  # menu "modificar cantidad de productos"

                    cantidad_producto = int(input("Ingresa nuevamente la cantidad del producto: "))
                    print(f"Completado, ahora la cantidad es de {cantidad_producto}")

            else:
                print("No hay productos disponibles todavia")



        elif opcion_usuario2 == 3:       # Este es el menu de eliminar producto
            print("Trabajo en progreso...")




        elif opcion_usuario2 == 4:         # Este es el menu de consultas de inventario
            print("Trabajo en progreso...")




        elif opcion_usuario2 == 5:
            print("Saliendo del programa...")













            # menu de ventas

    elif opcion_usuario == 2:          # Este es el menu de ventas
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
            print("Trabajo en progreso...")

        elif opcion_usuario2 == 4:
            print("saliendo del programa...")




                # menu de reportes generales

    elif opcion_usuario == 3:         # Este es el menu de reportes generales
        print( "Trabajo en progreso: ")




            # menu de reclamos

    elif opcion_usuario == 4:          # Este es el menu de reclamos

        nombre_usuario = input("Estimado usuario, digite su nombre para proceder ")

        cantidad_reclamos = int(input("Cuantos reclamos deseas ingresar? "))

        for i in range(cantidad_reclamos):
            pass  # Aqui se almacenaran los reclamos en una lista para despues guardarse en un archivo txt

        print("Trabajo en progreso...")




                # opcion para cerrar el programa


    elif opcion_usuario == 5:        # esta es la opcion para cerrar el programa
        validacion = False
        print("Saliendo del programa, !Gracias por preferirnos¡ ... ")









