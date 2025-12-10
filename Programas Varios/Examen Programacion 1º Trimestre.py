En este examen muestro mis conocimientos de programacion apartir de la creacion de un mini crud, al cual lo vinculo a una base de datos previamente creada para el examen de base de datos
#Nos conectamos con el usuario Manolo
conexion = mysql.connector.connect(
    host="localhost",
    user="Manolo",
    password="Portafolio123$",
    database="portafolioexamen"
)
#Damos los buenos dias
print("Buenas dias")
cursor = conexion.cursor()
#Iniciamos un bucle
while True:
		#Mostramos las opciones posibles
    print("Escoje una opcion: ")
    print("1.Insertar una pieza")
    print("2Listar clientes")
    print("3.Actualizar un cliente")
    print("4.Eliminar un cliente")
		Pedimos una de las 4 opciones previamente presentadas al usuario
    opcion = int(input("Escoje una opcion: "))
		#Se ejecutara esta seccion de codigo si se a introducido la opcion 1
    if opcion == 1:
        titulitis = input("Titulo: ")    
        descripcion = input("Descripcion: ")
        fecha = input("Fecha: ")
        id_categoria = input("id de la categoria:")

        sql = "insert into piezasportafolio (titulitis, descripcion, fecha, id_categoria) VALUES (%s,%s,%s,%s)"
        VALUES = (titulitis,descripcion,fecha,id_categoria)
        cursor.execute(sql, VALUES)
        conexion.commit()

        print("pieza insertada exitosamente")
		#Se ejecutara esta seccion de codigo si se a introducido la opcion 2
    elif opcion == 2:
        cursor.execute("Select * FROM piezasportafolio")
        filas = cursor.fetchall()
        for fila in filas:
            print(fila)
		#Se ejecutara esta seccion de codigo si se a introducido la opcion 3
    elif opcion == 3:
        id_pieza = input("Selecciona el id de la pieza a actualizar: ")
        nuevo_titulitis = input("Nuevo Titulo: ")
        sql = "UPDATE piezasportafolio SET titulitis = %s WHERE id =%s"
        cursor.execute(sql, (nuevo_titulitis,id_pieza))
        conexion.commit()
        print("Pieza actualizada correctamente")
		#Se ejecutara esta seccion de codigo si se a introducido la opcion 4
    elif opcion == 4:
        id_pieza = input("Elige el id de la pieza a eliminar: ")
        sql = "DELETE FROM piezasportafolio WHERE id = %s"
        cursor.execute(sql(id_pieza))
        conexion.commit
Conclusion
En este ejercicio enseño el como he aprendido a no solorealizar un CRUD sino tambien a como vincularle una base de datos, lo cual en un contexto en empresarial seria imprescindible, ya que agilizaria y haria extremadamente mas sencillo, especialmente para los no adeptos a la informatica a introducior, modificar, ver y eliminar datos de una base de datos aun sin saber programar
