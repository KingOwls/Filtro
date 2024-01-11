import funciones.generos as Gn
import funciones.actores as ac
import funciones.peliculas as pel
import funciones.formatos as form
import funciones.informes as info
def Gestor_Informes():
    ruptura = True
    while ruptura:
        print ("Gestor de Informes:")
        print("Seleccione uno para trabajar el dia de hoy")
        print("1)Listar las peliculas de un genero especifico")
        print("2)Listar las pelicuasl donde el protagonista sea Silvestre Stallone")
        print("3)Buscar pelicula y mostrar la sinopsis y los actores")
        print("4)ir al menu principal")
        Desicion = input("Escojaa de las sigueintes opciones:")
        if Desicion == "1":
            print("1)Listar las peliculas de un genero especifico")
            print("pause")
            info.Buscador_Especifico()
        elif Desicion == "2":
            print("2)Listar las pelicuasl donde el protagonista sea Silvestre Stallone")
            print("pause")
            info.Buscador_Actor
        elif Desicion == "3":
            print("3)Buscar pelicula y mostrar la sinopsis y los actores")
            print("pause")
            info.Buscar_SipAct()
        elif Desicion == "4":
            print("ir al menu principal")
            print("pause")
            ruptura = False
        else:
            print("Error en la eleccion, Ingrese una desicion correcta")
            print("pause")

def Gestor_Pelicula():
    ruptura = True
    while ruptura:
        print ("Bienvenido al programa de BlockBuster:")
        print("Seleccione uno para trabajar el dia de hoy")
        print("1)Agregar Peliculas")
        print("2)Editar Peliculas")
        print("3)Eliminar Peliculas")
        print("4)eliminar Actor")
        print("5)Buscar Pelicula")
        print("6)Lista todas las Peliculas")
        print("7)Salir")
        Desicion = input("Escojaa de las sigueintes opciones:")
        if Desicion == "1":
            print("1)Agregar Peliculas")
            print("pause")
            pel.Creador_Pelicula()
        elif Desicion == "2":
            print("2)Editar Peliculas")
            print("pause")
            pel.Editor_Pelicula()
        elif Desicion == "3":
            print("3)Eliminar Peliculas")
            print("pause")
            pel.Elminar_Pelicula()
        elif Desicion == "4":
            print("4)eliminar Actor")
            print("pause")
            pel.Elminar_Actor()
        elif Desicion == "5":
            print("5)Buscar Pelicula")
            print("pause")
            pel.Buscar_Pelicula()
        elif Desicion == "6":
            print("6)Lista todas las Peliculas")
            print("pause")
            pel.lista_Pelicula()
        elif Desicion == "7":
            print("7)Salir")
            print("pause")
            ruptura = False
        else:
            print("Error en la eleccion, Ingrese una desicion correcta")
            print("pause")

def Gestor_Formatos():
    ruptura = True
    while ruptura:
        print ("Gestor de generos:")
        print("Seleccione uno para trabajar el dia de hoy")
        print("1)Crear Formato")
        print("2)Lista de Formatos")
        print("3)ir al menu principal")
        Desicion = input("Escojaa de las sigueintes opciones:")
        if Desicion == "1":
            print("Crear Formato")
            print("pause")
            form.Creador_formato()
        elif Desicion == "2":
            print("Lista de Formatos")
            print("pause")
            form.Lista_formato()
        elif Desicion == "3":
            print("ir al menu principal")
            print("pause")
            ruptura = False
        else:
            print("Error en la eleccion, Ingrese una desicion correcta")
            print("pause")


def Gestor_Actores():
    ruptura = True
    while ruptura:
        print ("Gestor de generos:")
        print("Seleccione uno para trabajar el dia de hoy")
        print("1)Crear Actor")
        print("2)Lista de Actores")
        print("3)ir al menu principal")
        Desicion = input("Escojaa de las sigueintes opciones:")
        if Desicion == "1":
            print("Crear Actor")
            print("pause")
            ac.Creador_Actores()
        elif Desicion == "2":
            print("Lista de Actores")
            print("pause")
            ac.Lista_Actores()
        elif Desicion == "3":
            print("ir al menu principal")
            print("pause")
            ruptura = False
        else:
            print("Error en la eleccion, Ingrese una desicion correcta")
            print("pause")

def Gestor_Generos():
    ruptura = True
    while ruptura:
        print ("Gestor de generos:")
        print("Seleccione uno para trabajar el dia de hoy")
        print("1)Crear generos")
        print("2)Lista de generos")
        print("3)ir al menu principal")
        Desicion = input("Escojaa de las sigueintes opciones:")
        if Desicion == "1":
            print("Crear generos")
            print("pause")
            Gn.Creador_Genero()
        elif Desicion == "2":
            print("Lista de generos")
            print("pause")
            Gn.Lista_Genero()
        elif Desicion == "3":
            print("ir al menu principal")
            print("pause")
            ruptura = False
        else:
            print("Error en la eleccion, Ingrese una desicion correcta")
            print("pause")

def MenuPrincipal():
    ruptura = True
    while ruptura:
        print ("Bienvenido al programa de BlockBuster:")
        print("Seleccione uno para trabajar el dia de hoy")
        print("1)Admiminstracion de generos")
        print("2)Admiminstracion de Actores")
        print("3)Admiminstracion de formato")
        print("4)Gestion de informes")
        print("5)Gestiom de peliculas")
        print("6)Salir")
        Desicion = input("Escojaa de las sigueintes opciones:")
        if Desicion == "1":
            print("Admiminstracion de generos")
            print("pause")
            Gestor_Generos()
        elif Desicion == "2":
            print("Admiminstracion de actores")
            print("pause")
            Gestor_Actores()
        elif Desicion == "3":
            print("Admiminstracion de Formato")
            print("pause")
            Gestor_Formatos()
        elif Desicion == "4":
            print("Gestion de informes")
            print("pause")
            Gestor_Informes()
        elif Desicion == "5":
            print("Gestion de peliculas")
            print("pause")
            Gestor_Pelicula()
        elif Desicion == "6":
            print("Salir")
            print("pause")
            ruptura = False
        else:
            print("Error en la eleccion, Ingrese una desicion correcta")
            print("pause")