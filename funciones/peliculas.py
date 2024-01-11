import funciones.corefile as cr
import funciones.actores as act
import funciones.formatos as form
import funciones.generos as gn
blockbuster:{
    "peliculas":{
        "P01":{
            "id" : "P01",
            "name" : "",
            "duracion":"",
            "Sinopsis":"",
            "generos":{
                "G01":{
                "id" : "G01",
                "nombre":""
                }
            },
            "Actores":{
                "A01":{
                    "id" : "A01",
                    "nombre":"",
                    "roles":"Protragonista o antagonista o reparto"
                }
            },
            "formato":{
                "F01":{
                    "id" : "F01",
                    "nombre":"DVD",
                    "Nrocopias": 2,
                    "ValorPrestamo": 5000
                },
                "F02":{
                    "id" : "F02",
                    "nombre":"Blueray",
                    "Nrocopias": 2,
                    "ValorPrestamo": 8000
                }
            }
        }
    }
}
def Creador_Pelicula():
    print("Creando Pelicula")
    Pelicula = input("Ingrese el Pelicula que quiere agregar")
    UBICAION ="Peliculas.json"
    for i, key in Pelicula.value():
        input(f" Ingrese el atributo del Pelicula"[key])
    cr.escritura(UBICAION, Pelicula)

def Editor_Pelicula():
    URL = "peliculas.json"
    for i in Pelicula:
        for key in pelicula.keys():
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
    pass
def Elminar_Actor():
    pass
def Buscar_Pelicula():
    pass
def lista_Pelicula():
    pass
