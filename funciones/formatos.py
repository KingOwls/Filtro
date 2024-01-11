import funciones.corefile as cr
formatos:{
    "F01":{
        "id" : "F01",
        "nombre":"DVD",
    }
}

def Creador_formato():
    print("Creando formato")
    formato = input("Ingrese el formato que quiere agregar")
    UBICAION ="formatos.json"
    Discancia_formato= input("Deme el codigo del formato")
    formatos:{
        Discancia_formato:{
            Discancia_formato,
            formato
        }
    }
    cr.escritura(UBICAION, formato)

def Lista_formato():
    for key, value in formatos.items():
        print(key)