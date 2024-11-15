from datetime import datetime

patrones_fecha = ["%Y-%m-%d", 
                  "%d/%m/%Y", 
                  "%m-%d-%Y", 
                  "%d-%m-%Y", "%Y/%m/%d"]

def determinar_tipo(cadena):
    if cadena.isdigit():
        return "Numero"

    for patron in patrones_fecha:
        try:
            datetime.strptime(cadena, patron)
            return "Fecha"
        except ValueError:
            continue

    return "Texto"


def tipo_fecha(cadena):
    for patron in patrones_fecha:
        try:
            return datetime.strptime(cadena, patron)
        except ValueError:
            continue
