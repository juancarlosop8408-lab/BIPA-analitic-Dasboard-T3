import pandas as pd

def cargar_datos():

    items = pd.read_csv(
        "data/Items.csv",
        encoding="latin1"
    )

    prestamos = pd.read_csv(
        "data/Prestamos.csv",
        encoding="latin1"
    )

    usuarios = pd.read_csv(
        "data/Usuarios.csv",
        encoding="latin1"
    )

    lcc = pd.read_csv(
        "data/Clasificacion LCC.csv",
        encoding="latin1"
    )

    return items, prestamos, usuarios, lcc