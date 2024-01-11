import funciones.corefile as cr
import json as json 
def Creador_Genero():
    UBICAION ="generos.json"
    print("Creando Genero")
    genero = input("Ingrese el genero que quiere agregar")
    Discancia_Genero= int(input("Deme el codigo del Genero"))
    Lista:{
            "Id": Discancia_Genero ,
            "Name": genero
    }
    json.dump(Lista, genero, Discancia_Genero)
    cr.loadData(Lista, UBICAION)


def Lista_Genero():
    UBICAION ="generos.json"
    Listado = cr.loadData(UBICAION)
    for key in Listado.items():
        print(key)