import funciones.corefile as cr





def Creador_Genero():
    UBICAION ="generos.json"
    print("Creando Genero")
    genero = input("Ingrese el genero que quiere agregar")
    Discancia_Genero= int(input("Deme el codigo del Genero"))
    Lista:{
            "Id": Discancia_Genero ,
            "Name": genero
    }

    cr.loadData(Lista, UBICAION)


def Lista_Genero():
    for key, value in Generos.items():
        print(key)