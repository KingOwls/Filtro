import funciones.corefile as cr
import funciones.actores as act
import funciones.formatos as form
import funciones.generos as gn
import json as pel

def Creador_Pelicula():
    print("Creando Pelicula")
    Peliculas = input("Ingrese el Pelicula que quiere agregar")
    UBICAION ="Peliculas.json"
    pelicula =input("pelicula")
    id =input("id")
    name =input("name")
    duracion = input("duracion")
    sinopsis =input("Sinopsis")
    genero =input("generos")
    actores =input("Actores")
    formato = input("formato")
    id:{
        pelicula, 
        id,
        name,
        duracion,
        sinopsis,
        genero,
        actores,
        formato
    }
    cr.loadData(dict, UBICAION)

def Editor_Pelicula():
    URL = "peliculas.json"
    cr.loadData(dict, URL)
    
    for i in Peliculas:
        for key in peliculas.keys():
            Desicion = input(f"Desea editar la seccion {i[key]} de la pelicula? S para si, espacio para no")
            if Desicion == "S":
                input(f"Inserte el nuevo{i} de la pelicula?")
                break
    pass


def Elminar_Pelicula():
    Destruccion = int(input("De el codigo de la pelicula a elimnar"))
    for i in lista_Pelicula():
        for key in lista_Pelicula.keys():
            if key == Destruccion:
                pop.pelicula(i)

def Elminar_Actor():
    Destruccion = int(input("De el codigo del actor a elimnar"))
    for i in act.Lista_Actores():
        for key in act.Lista_Actores():
            if key == Destruccion:
                pop.pelicula(i)

def Buscar_Pelicula():
    URL = "peliculas.json"
    buscador = int(input("Pelicula a buscar..."))
    for i, key in cr.loadData(URL):
        if key == buscador:
            print(f"la pelicula es {i[key]} y su sinopsis es sinopsis" )

def lista_Pelicula():
    URL = "peliculas.json"
    for i in cr.loadData(URL):
        print(i[name])

