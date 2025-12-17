
from funciones.funciones import *
from CRUD.CRUD_notas_credito import *

def cargar_nc(fecha_ing):
    fecha = validar_fecha(fecha_ing)
    fecha_limite = datetime.now().date()
    #TRANSACCION-0 FECHA-1 HORA-2 CAJERO-3 MONTO-4 CORRELATIVO-5 SERIE-6
    matriz = todas_trans(fecha, fecha_limite)
    datos = []
    for row in matriz:
        id = row[0] + str(row[1])
        datos.append(id)
        for elemento in row:
            datos.append(elemento)
        #datos.append(id)
        registrar_nc(datos)
        #for elemento in row:
        datos.clear()
    print("Completado")
