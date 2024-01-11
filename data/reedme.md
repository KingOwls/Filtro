import os
import controllers.clientes as clientServices
import templates.menus as menus


if __name__ == "__main__":
    while(True):
        opMenu = input(menus.printMenus("main"))
        if(opMenu == "1"):
            clientServices.menu()
        elif(opMenu == "2"):
            pass
        elif(opMenu == "3"):
            pass
        elif(opMenu == "4"):
            break
        else:
            print(menus.valueErrorMessage)

        os.system("pause")


    header = "SISTEMA GESTOR DE INVENTARIOS"
opcions = [
    'Gestor Clientes',
    'Gestor Proveedores',
    'Gestor Productos',
    'Salir'
]

valueErrorMessage = "Opcion No Valida.."


def printMenus(header, opcions):
    headerT = f"+ {header} +"
    lenHeader = len(headerT)
    print("+"*lenHeader)
    print(headerT)
    print("+"*lenHeader)
    print("")
    for i, item in enumerate(opcions):
        print(f"{i+1}.{item}")
    print("")
    return ":> "



import controllers.db as db
import templates.menus as menus
import controllers.reusable as reusable

#db
db.URL = "/data/db.json"

#TEMPLATES
header = "ADMINISTRACION DE CLIENTES"
opcions = [
    'Nuevo Cliente',
    'Borrar Cliente',
    'Editar Cliente', 
    'Buscar',
    'Menu Principal'
]

cliente = {
    "cc": "",
    "nombre": "",
    "apellidos": "",
    "email_personal": "",
    "email_empresarial": "",
    "edad": 0,
    "telefonos": []
}



def menu():
    while(True):
        op = input(menus.printMenus(header, opcions))
        if(op == "1"):
            for key, value in cliente.items():
                cliente[key] = input(f"Ingresa {key.upper()} del Cliente")
                if type(value) == int:
                    cliente[key] = reusable.checkInput("int",f"Ingresa {key.upper()} del Cliente")
                elif type(value) == list:
                    pass
        elif(op == "5"):
            return
        else:
            print(menus.valueErrorMessage)


def newClient():
    pass
import json
import os

PATH = "./Inventario Archivos/data/"
URL = ''

def saveData(**data):
    with open(f"{PATH}{URL}", "w") as archivo:
        json.dump(data, archivo, indent=4)

def loadData(**data):
    file = os.path.isfile(f"{PATH}{URL}")
    if(not file):
        saveData(**data)
        return data
    else:
        with open(f"{PATH}{URL}", "r") as archivo:
            return json.load(archivo)
import os


def showError(message):
    pass

def showSuccess():
    pass


def checkInput(typeData,message):
    while True:
        try:
            if typeData == "int":
                number = int(input(message))
            elif typeData == "float":
                number = float(input(message))
        except ValueError:
            print("Error Al Ingresar el Dato Solo Ingresa Numeros....")
        else:
            return number