import pyodbc
import subprocess
import sys, os

# Configuración de la conexión
def conexion_ddbb_antigua():
    server = r'192.168.3.96\SQLEXPRESS'
    database = 'CTASXCOBRAR'
    username = 'daxerder'
    password = 'danebalto'
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'


    # Conectar a la base de datos
    try:
        conn = pyodbc.connect(connection_string)
        #conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        return conn
    except pyodbc.Error as e:
        print("Error en la conexión:", e)

def conexion_sql():
    server = r'192.168.3.5'
    database = 'BD_SALIDAS'
    username = 'Alex'
    password = 'Finanzas123'
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    try:
        conn = pyodbc.connect(connection_string)
        #conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        return conn
    except pyodbc.Error as e:
        print("Error en la conexión:", e)

def conexion_ddbb():
    server = r'192.168.3.5'
    database = 'FINANZAS'
    username = 'Alex'#Alex
    password = 'Finanzas123'#Finanzas123
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except pyodbc.Error as e:
        print("Error en la conexión:", e)