import tkinter as tk
import tempfile
import os

def crear_y_abrir_txt(tupla):
    # Crear un archivo temporal
    archivo_temporal = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
    for string in tupla:
        try:
            # Escribir contenido en el archivo temporal
            archivo_temporal.write(str(string).encode('utf-8'))
            archivo_temporal.write("\n".encode('utf-8'))
            
        except Exception as e:
            print(f"Error -> {e}")
        
    archivo_temporal.close()
    os.system(f'notepad {archivo_temporal.name}')