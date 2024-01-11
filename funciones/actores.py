import funciones.corefile as cr

def Creador_Actores():
    Actores:{
    1:{
        "id" : 1,
        "nombre":""
        }
}
    UBICAION ="Actores.json"
    cr.escritura(UBICAION, Actores)
    print("Creando Actores")
    Actor = input("Ingrese el Actores que quiere agregar")
    UBICAION ="Actores.json"
    Discancia_Actores= input("Deme el codigo del Actores")
    Actores:{
        Discancia_Actores:{
            "id" : Discancia_Actores,
            "nombre":Actor
        }
    }
    cr.escritura(UBICAION, Actores)

def Lista_Actores():
    for key, value in Actores.items():
        print(key)
    pass