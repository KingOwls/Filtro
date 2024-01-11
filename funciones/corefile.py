import json as json
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

Actores:{
    "A01":{
    "id" : "A01",
    "nombre":"",
    "roles":"Protragonista o antagonista o reparto"
    }
}

generos:{
    "G01":{
        "id" : "G01",
        "nombre":""
    }
}
formato:{
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


PATH = "data/"
URL = ''
def escritura(data, URL):
    with open(f"{PATH}{URL}", "w") as archivo:
        json.dump(data, archivo, indent=4)

    pass

def loadData(data, URL):
    file = (f"{PATH}{URL}")
    if(not file):
        escritura(data, URL)
        return data
    else:
        with open(f"{PATH}{URL}", "r+") as archivo:
            return json.load(archivo)