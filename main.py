import os

            # Funciones de los menus principales

def menu_inventario(cantidad):  # menu del inventario

    print("Bienvenido al inventario: ")

    print("(1)  Agregar productos")
    print("(2)  Modificar productos")
    print("(3)  Eliminar producto")
    print("(4) consultas de inventario")
    print("(5)  Devolverse al menu principal")

    opcion_usuario2 = int(input("Digite la opcion que necesita: "))

    if opcion_usuario2 == 1:  # Este es el menu de agregar productos
        cantidad = int(input("Cuantos productos desea ingresar: "))

        for i in range(cantidad):  # Aqui se ingresan los datos especificos de cada producto
            producto_agregado = {}

            nombre_producto = input("Ingresa el nombre del producto: ")
            precio_producto = int(input("Ingresa el precio del producto: "))
            cantidad_producto = int(input("Ingresa el cantidad del producto: "))
            codigo_producto = int(input("Ingresa el codigo del producto: "))

            producto_agregado = {'nombre': nombre_producto, "precio": precio_producto, "cantidad": cantidad_producto, "codigo": codigo_producto}

            inventario.append(producto_agregado)  # con la metodo append se agrega el diccionario a la lista del inventario
            print("Productos agregados correctamente al inventario.... ")

            producto_agregado = {}  # el diccionario se limpia, para poder seguir agregando otros productos y que no se colapse de informacion


    elif opcion_usuario2 == 2:  # Este es el menu de modificar productos

        if cantidad != 0:
            print(f"Productos disponibles")
            mostrar_productos()

            producto_escogido = (int(input("Que producto deseas escoger? ")))
            producto_escogido = inventario[producto_escogido]  # se le asigna a la variable el diccionario escogido

            print(f"producto escogido: {producto_escogido['nombre']}")

            print("(1) - Nombre")
            print("(2) - Precio")
            print("(3) - Cantidad")
            print("(4) - Codigo")

            opcion = int(input("Que deseas modificar: "))

            if opcion == 1:  # menu "modificar el nombre de producto"

                nombre_producto = input("Ingresa nuevamente el nombre del producto ")
                modificar_producto(producto_escogido, nombre_producto, elemento="nombre")

            elif opcion == 2:  # menu "modificar el precio de proucto"

                precio_producto = int(input("Ingresa nuevamente el precio del producto "))
                modificar_producto(producto_escogido, precio_producto, elemento="precio")

            elif opcion == 3:  # menu "modificar cantidad de productos"

                cantidad_producto = int(input("Ingresa nuevamente la cantidad del producto: "))
                modificar_producto(producto_escogido, cantidad_producto, elemento="cantidad")

            elif opcion == 4:  # menu "modificar codigo de productos"

                codigo_producto = int(input("Ingresa nuevamente el codigo del producto: "))
                modificar_producto(producto_escogido, codigo_producto, elemento="codigo")

        else:
            print("No hay productos disponibles todavia")



    elif opcion_usuario2 == 3:  # Este es el menu de eliminar producto
        print(f"Productos disponibles")
        mostrar_productos()

        producto_escogido = (int(input("Que producto deseas eliminar? ")))

        inventario.pop(producto_escogido)   # el metodo pop elimina el elemento seleccionado de la lista de inventario
        print("El producto se ha eliminado exitosamente...")


    elif opcion_usuario2 == 4:  # Este es el menu de consultas de inventario
        print("Bienvenido al menu de consultas de inventario")
        print("(1) Consultar por codigo")
        print("(2) Consulta general")
        print("(3) Consultar por precio")
        print("(4) Desplegar a un archivo plano el inventario completo")

        opcion_usuario2 = int(input("Digite la opcion que necesita: "))

        if opcion_usuario2 == 1:  # menu consulta por codigo

            codigo_buscador = int(input("Ingresa el codigo que buscas: "))
            producto = buscar_porDato(codigo_buscador, elemento="codigo")

            pregunta_consulta = input("Ingresa 1 si deseas desplegar este inventario a un archivo plano: ")

            if pregunta_consulta == "1":
                crear_archivo(producto)

        elif opcion_usuario2 == 2:    # menu de consulta general
            print(f"Productos disponibles")
            mostrar_productos()


        elif opcion_usuario2 == 3:  # menu consulta por precio

            codigo_buscador = int(input("Ingresa el precio de producto que buscas: "))
            producto = buscar_porDato(codigo_buscador, elemento="precio")

            pregunta_consulta = input("Ingresa 1 si deseas desplegar este inventario a un archivo plano: ")

            if pregunta_consulta == "1":
                crear_archivo(producto)


        elif opcion_usuario2 == 4:  # menu de consulta por arhivo de texto plano

            crear_archivo(inventario)


    elif opcion_usuario2 == 5:
        print("Saliendo del menu...")


def menu_ventas():

    print("Bienvenido al menu de ventas: ")

    print("(1)  Mostrar productos disponibles: ")
    print("(2)  Realizar la venta: ")
    print("(3)  Generar factura final ")
    print("(4)  Devolverse al menu principal:")

    opcion_usuario2 = int(input("Digite la opcion que necesita: "))

    if opcion_usuario2 == 1:
        print("Productos disponibles: ")
        mostrar_productos()

    elif opcion_usuario2 == 2:

        x = 0  # Se define a x como la condicional que nos dicta si se encontro un producto o no
        compra = int(input("Ingrese el codigo de la prenda: "))

        for i in inventario:
            x = i.get("codigo")

            if int(x) == compra:
                x += 1  # Se encontro el producto, por lo tanto, x es igual a 1
                cantidad = int(input("Digite la cantidad que desea comprar: "))

                if i.get("cantidad") < cantidad:
                    print("La cantidad ordenada excede la cantidad disponible")

                if i.get("cantidad") >= cantidad:

                    nombre = input("Ingrese su nombre: ")
                    cedula = int(input("Digite su cedula: "))
                    telefono = int(input("Digite su numero de telefono: "))
                    direccion = input("Ingrese su direccion: ")
                    desc = 0

                    total = cantidad * i.get("precio")
                    if cantidad >= 5:
                        total = total * 0.85
                        desc = 1

                    if desc == 1:
                        venta_agregada = {'nombre': nombre, "cedula": cedula,
                                          "telefono": telefono, "direccion": direccion,
                                          "producto": i.get("nombre"), "cantidad": cantidad,
                                          "total": total, "descuento": "15%"}
                    else:
                        venta_agregada = {'nombre': nombre, "cedula": cedula,
                                          "telefono": telefono, "direccion": direccion,
                                          "producto": i.get("nombre"), "cantidad": cantidad,
                                          "total": total, "descuento": 0}

                    historial_venta.append(venta_agregada)

                    print("La factura es la siguiente: ")

                    print("nombre: ", venta_agregada.get("nombre"))
                    print("cedula: ", venta_agregada.get("cedula"))
                    print("telefono: ", venta_agregada.get("telefono"))
                    print("direccion: ", venta_agregada.get("direccion"))
                    print("producto: ", venta_agregada.get("producto"))
                    print("cantidad: ", venta_agregada.get("cantidad"))
                    print("descuento: ", venta_agregada.get("descuento"))
                    print("total: ", venta_agregada.get("total"))
                    temp = i.get("cantidad")
                    temp = temp - cantidad
                    i["cantidad"] = temp


                    nombre_archivo = input("Ingresa el nombre que le deseas dar a la factura: ")
                    ubicacion = "Archivos/" + nombre_archivo + ".txt"

                    print("El archivo se esta guardando....")

                    with open(ubicacion, "a", encoding="utf-8") as f:

                        f.write("-----------Factura Sistema Pyme--------------")
                        f.write("\n")
                        f.write(f"nombre: {venta_agregada.get('nombre')} \n")
                        f.write(f"cedula: {venta_agregada.get('cedula')} \n")
                        f.write(f"telefono: {venta_agregada.get('telefono')} \n")
                        f.write(f"direccion: {venta_agregada.get('direccion')} \n")
                        f.write(f"Producto: {venta_agregada.get('producto')} \n")
                        f.write(f"cantidad: {venta_agregada.get('cantidad')} \n")
                        f.write(f"descuento: {venta_agregada.get('descuento')} \n")
                        f.write("\n")
                        f.write("------Total----------")
                        f.write("\n")
                        f.write(f"total: {venta_agregada.get('total')} \n")
                        f.close()

                        print("La informacion fue grabada correctamente! ")

                    venta_agregada = {}


        if x == 0:  # Si la funcion termina  y x es igual a 0 significa que no se encontro ese producto
            print("Este producto no existe")



def menu_reportesGenerales():             # hasta trabajar con archivos planos se agregara este menu

    print("(1)  Promedio de ventas general")
    print("(2)  Promedio de ventas por producto")
    print("(3)  Ventas mas alta realizada")
    print("(4)  Productos agotados")
    print("(5)  Productos disponibles")

    opcion_usuario5 = int(input("Digite la opcion que necesita: "))

    if opcion_usuario5 == 1:

        print("El promedio de ventas es el siguiente: ")
        sumatoria = 0

        for i in inventario:
            sumatoria += i.get("cantidad")

        promVentas = len(historial_venta) / cantidad

        print("el promedio de ventas generales es: ", promVentas)


    # pendiente
    elif opcion_usuario5 == 2:
        print("El promedio de ventas por producto es el siguiente")
        pass


    elif opcion_usuario5 == 3:
        print("la venta mas alta realizada es la siguiente: ")

        mayor = 0
        nombre_producto = 0

        for i in historial_venta:
            if i.get("total") > mayor:
                mayor = i.get("total")
                nombre_producto = i.get("nombre")
                tipo_producto = i.get("producto")

        print(f"La venta mas alta realizada fue la de {nombre_producto}, producto = {tipo_producto}, con un total de {mayor}")


    elif opcion_usuario5 == 4:
        print("los productos agotados son los siguientes")


        cantidad_agotados = 0

        if len(inventario) != 0:
            for i in inventario:
                if i.get("cantidad") == 0:
                    print(f"El producto {i.get('nombre')} esta agotado")
                    cantidad_agotados += 1

        if cantidad_agotados == 0:
            print("No hay productos agotados..")


    elif opcion_usuario5 == 5:
        mostrar_productos()



def menu_reclamos(reclamos_inventario):
    print("Menú de reclamos")

    print("(1)  Anotar el reclamos correspondientes")
    print("(2)  Cantidad de reclamos ingresados")
    print("(3)  Devolverse al menú principal")

    opcion_usuario4 = int(input("Digite la opcion que necesita: "))

    if opcion_usuario4 == 1:

        reclamo_agregado = {}
        print("Complete la siguiente informacion: ")

        nombre_completo = input("Ingrese su nombre completo: ")
        numero_telefonico = int(input("Ingrese su número de telefono: "))
        correo_electronico = input("Ingrese su correo electronico: ")

        reclamo_agregado = {'nombre': nombre_completo, "numero_tel": numero_telefonico, "correo": correo_electronico}
        print("Informacion guardada correctamente....")

        ingresar_reclamo = input(f"redacte su reclamo: ")
        reclamo_agregado["reclamo"] = ingresar_reclamo

        reclamos_inventario.append(reclamo_agregado)  # con la metodo append se agrega el diccionario a la lista del inventario de reclamos
        print("¡Gracias por sus observaciones los reclamos han sido guardados correctamente!")
        print("Si querés una observación más detalla sobre tu problema mandanos tus consultas a este correo PymesTrajescr@gmail.com")



    elif opcion_usuario4 == 2:

        print(f"Reclamos ingresados")
        contador = 0  # este contador sirve para numerar los tipos de productos

        for i in reclamos_inventario:
            print(f"({contador+1}) Nombre: {i['nombre']}", end=' , ')
            print(f"numero telefono: {i['numero_tel']}", end=' , ')
            print(f"correo: {i['correo']}", end=' , ')
            print(f"reclamo: {i['reclamo']}", end='  ')
            print("")
            contador += 1



# Funciones que sirven como herramientas para los menus, para no repetir codigo

def buscar_porDato(codigo_buscador, elemento):
    inventario_productoE = []   # esta lista sirve para guardar los datos buscados

    for i in inventario:

        if i[elemento] == codigo_buscador:
            print(f"El producto buscado es {i}")
            inventario_productoE.append(i)
            return inventario_productoE


def mostrar_productos():

    contador = 0  # este contador sirve para numerar los tipos de productos

    for i in inventario:
        print(f"({contador}) Nombre: {i['nombre']}", end=' , ')
        print(f"Precio: {i['precio']}", end=' , ')
        print(f"Cantidad: {i['cantidad']}", end=' , ')
        print(f"Codigo: {i['codigo']}", end='  ')
        print("")
        contador += 1

def modificar_producto(producto_escogido, nombre_producto, elemento):
    producto_escogido[elemento] = nombre_producto
    print(f"Completado, ahora el {elemento} es {nombre_producto}")



def crear_archivo(lista):

    nombre = input("Ingresa el nombre que le deseas dar al archivo: ")


    ubicacion = "Archivos/" + nombre + ".txt"

    print("El archivo se esta guardando....")

    with open(ubicacion, "a", encoding="utf-8") as f:

        contador = 0  # este contador sirve para numerar los tipos de productos

        for i in lista:
            f.write(f"({contador}) Nombre: {i['nombre']} ")
            f.write(f"Precio: {i['precio']} ")
            f.write(f"Cantidad: {i['cantidad']} ")
            f.write(f"Codigo: {i['codigo']} ")
            contador += 1
            f.write("\n")

    print("El archivo se ha guardado correctamente....")



def mostrar_archivo(nombre):

    print(f"Cargando el contenido del archivo '{nombre}'....")

    ubicacion = "Archivos/" + nombre + ".txt"
    contenido = []

    with open(ubicacion, "r", encoding="utf-8") as f:
        for line in f:
            contenido.append(str(line))
    print("El contenido del archivo es ")
    print(contenido)



# inicio del programa

if __name__ == '__main__':

    # inventario predeterminado productos

    pantalonetas_azules = {"nombre": "Pantalonetas Azules", "precio": 12000, "cantidad": 10, "codigo": 1212}
    bikinis_rojos = {"nombre": "Bikinis Rojos", "precio": 15000, "cantidad": 15, "codigo": 2222}
    pantalonetas_verdes = {"nombre": "Pantalonetas Verdes", "precio": 12000, "cantidad": 10, "codigo": 1111}


    inventario = [pantalonetas_azules, bikinis_rojos,pantalonetas_verdes]  # lista que almacena todos los direccionarios, "productos con sus datos"
    cantidad = len(inventario)  # el metodo len nos da la longitud de indices del inventario, para saber su cantidad especifica de productos

            # inventario reclamos e historial de ventas

    historial_venta = [{'nombre': 'Alejandro',
                        'cedula': 777777,
                        'telefono': 33333,
                        'direccion': '265 este de nose',
                        'producto': 'Pantalonetas Azules',
                        'cantidad': 3,
                        'total': 36000,
                        'descuento': 0}
                       ]

    reclamos_inventario = []

    while True:  # Este while nos permite crear un bucle al menu principal

        print("Bienvenido al sistema en linea de vestidos de baño")

        print("(1)  Inventario")
        print("(2)  ventas")
        print("(3)  Reportes Generales")
        print("(4)  Reclamos")
        print("(5) Salir")

        opcion_usuario = int(input("Digite la opcion que necesita: "))

        # menu de inventario

        if opcion_usuario == 1:
            menu_inventario(cantidad)

                # menu de ventas

        elif opcion_usuario == 2:  # Este es el menu de ventas
            menu_ventas()

        elif opcion_usuario == 3:  # Este es el menu de reportes generales  esto se continuara hasta trabajar con archivos de texto plano
            menu_reportesGenerales()

            # menu de reclamos

        elif opcion_usuario == 4:  # Este es el menu de reclamos
            menu_reclamos(reclamos_inventario)


            # salir del programa

        elif opcion_usuario == 5:  # esta es la opcion para cerrar el programa
            print("Saliendo del programa, !Gracias por preferirnos¡ ... ")
            break












