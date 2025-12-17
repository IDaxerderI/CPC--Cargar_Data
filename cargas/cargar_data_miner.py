import os
import openpyxl
from CRUD.CRUD_data_miner import *

from datetime import date
import subprocess
import sys, os
from funciones.funciones import *

def cargar_data_miner_dia(serie,fecha):
    venta_diaria  = consulta_vta_diaria(fecha,serie)
    for venta_caja in venta_diaria:
        datos=[venta_caja[0],
            venta_caja[1],
            venta_caja[2],
            venta_caja[3],
            serie,
            venta_caja[5],
            ]
        registrar_data_miner(datos)
        datos.clear()
    print(f"Completado dia {fecha}")

def eliminar_fecha_tienda(serie,fecha):
    eliminar_data_miner_dia(fecha,serie)
    print(f"Eliminado dia {fecha} serie: {serie}")