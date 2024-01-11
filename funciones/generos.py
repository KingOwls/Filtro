import funciones.corefile as cr
import json as json 
def Creador_Genero():
    UBICAION ="generos.json"
    print("Creando Genero")
    genero = input("Ingrese el genero que quiere agregar")
    Discancia_Genero= input("Deme el codigo del Genero")
    Genero : {
            "Id": Discancia_Genero ,
            "Name": genero
    }
    cr.loadData(dict, UBICAION) 


def Lista_Genero():
    UBICAION ="generos.json"
    Listado = cr.loadData(UBICAION)
    for key in Listado.items():
        print(key)