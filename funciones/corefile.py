import json as json
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