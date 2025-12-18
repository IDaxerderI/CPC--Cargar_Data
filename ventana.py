from tkinter import *
from tkinter import Tk, Label, Button, messagebox, ttk, Toplevel
import tkinter.font as tkfont
from tkinter import filedialog
import sys, os
from PIL import Image as IMG , ImageTk, ImageSequence

from datetime import datetime
from CRUD.CRUD_tiendas import todas_tiendas

from cargas.cargar_data_miner import cargar_data_miner_dia, eliminar_fecha_tienda
from cargas.cargar_notas_credito import cargar_nc
from cargas.cargar_tc_rc import cargar_recargo_cambio, actualizar_recargo_cambio
from cargas.cargar_personal import cargar_personal, actualizar_personal
from cargas.cargar_peya import cargar_peya
from cargas.cargar_tarjetas import cargar_tarjetas_izipay
from cargas.cargar_tiendas import actualizar_tiendas

from funciones.funciones import *

ventana = Tk()
ventana_ancho = 450
ventana_largo = 180
ventana.geometry(f"{ventana_ancho}x{ventana_largo}+10+10")
ventana.title("Cargar Datos")

V_Opcion = StringVar()
V_Barra = IntVar()
porcentaje = StringVar()
V_fecha = StringVar()
V_tienda = StringVar()
V_archivo = StringVar()

#icono = PhotoImage(file=ubicacion)
#ventana.iconphoto(False, icono, icono)

notas = todas_tiendas()
series = []
tiendas = []

#####################################################################################
###########-ESTILO LETRAS-###########################################################

fontStyle = tkfont.Font(family="Helvetica",size=10,weight="bold")
textStyle = tkfont.Font(family="Helvetica",size=9)
buttonStyle = tkfont.Font(family="Helvetica",size=10,weight="bold")
color_fondos = '#fdf7e7'
fondo_activo_boton = '#fdf7e7'

#####################################################################################
path = os.path.dirname(sys.executable) + "/icon"#paara ejecutable
path = "icon"
ubicacion = path + "/fondo.png"
fondo_imagen = PhotoImage(file=ubicacion)
ubicacion = path + "/logo.png"
icon_logo = PhotoImage(file=ubicacion).subsample(2, 2)

#####################################################################################
###########-CANVAS-##################################################################
canvas = Canvas(ventana)
canvas.create_image(0, 0, image=fondo_imagen, anchor=NW)

canvas.place(x=0, y=0, width=ventana_ancho, height=ventana_largo)
#####################################################################################
####-PROVISIONAL-####################################################################
if False:
    def dibujar_punto(x, y, radio=1):
        # El óvalo se dibuja desde (x-radio, y-radio) hasta (x+radio, y+radio)
        canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="red", outline="")

    def dibujar_numero(x, y, numero):
        canvas.create_text(x, y-10, text=numero)

    for fila in range (35,ventana_largo,35):
        contador = 10
        divisor = 10
        for columna in range (10,ventana_ancho,10):
            
            dibujar_punto(columna, fila)
            
            if contador % divisor == 0 and (contador/divisor < 2 or (contador/divisor) % divisor == 0):
                dibujar_numero(columna, fila, contador)
            contador += 10
            
            #pass

#####################################################################################
#####################################################################################

for fila in notas:
    series.append(fila[0])
    tiendas.append(fila[1])

#####################################################################################
#####################################################################################

def ret_serie():
    selected_tienda = E_Tiendas.get()  # Obtener tienda seleccionada
    indice = tiendas.index(selected_tienda)
    serie = series[indice]
    return serie

def seleccionar_archivo():
    filename = filedialog.askopenfilename()
    if filename:
        V_archivo.set(filename)
    else:
        pass

#####################################################################################
#####################################################################################

def cargar():
    opcion = V_Opcion.get()
    try:
        cambio_fecha()
    except:
        pass
    
    if opcion == "Peya":
        cargar_peya(V_archivo.get())
    
    elif opcion == "Tarjetas":
        cargar_tarjetas_izipay(V_archivo.get())
    
    elif opcion == "Tiendas":
        pass
    
    elif opcion == "Personal":
        cargar_personal(V_archivo.get())
    
    elif opcion == "Notas de Credito":
        cargar_nc(V_fecha.get())
    
    elif opcion == "Cargar RC - TC":
        cargar_recargo_cambio(V_archivo.get())
    
    elif opcion == "Data Miner":
        cargar_data_miner_dia(ret_serie(),E_Fecha.get())

def actualizar():
    opcion = V_Opcion.get()
    try:
        cambio_fecha()
    except:
        pass
    
    if opcion == "Peya":
        #actualizar_peya(V_archivo.get())
        pass
    
    elif opcion == "Tarjetas":
        pass
    
    elif opcion == "Tiendas":
        actualizar_tiendas(V_archivo.get())
    
    elif opcion == "Personal":
        actualizar_personal(V_archivo.get())
    
    elif opcion == "Anulaciones C.C.":
        #actualizar_cc()
        pass
    
    elif opcion == "Cargar RC - TC":
        actualizar_recargo_cambio(V_archivo.get())

def eliminar():
    try:
        cambio_fecha()
    except:
        pass
    opcion = V_Opcion.get()
    
    if opcion == "Peya":
        #eliminar_peya(V_fecha.get())
        pass
    
    elif opcion == "Tarjetas":
        #eliminar_tarjetas(V_fecha.get())
        pass
    
    elif opcion == "Trabajadores":
        #eliminar_personal()
        pass
    
    elif opcion == "Data Miner":
        serie = ret_serie()
        eliminar_fecha_tienda(serie,E_Fecha.get())

#####################################################################################
#####################################################################################

def cambio_fecha():
    fecha = validar_fecha(V_fecha.get())
    V_fecha.set(fecha)

def habilitar_fecha(event):
    if V_Opcion.get() == "Notas de Credito":
        E_Fecha.config(state= "normal")
        E_Tiendas.config(state=DISABLED)
        V_tienda.set("")

    elif V_Opcion.get() == "Peya":
        E_Fecha.config(state= "normal")
        E_Tiendas.config(state=DISABLED)
        V_tienda.set("")

    elif V_Opcion.get() == "Movimientos Bancarios Soles":
        E_Fecha.config(state= "normal")
        E_Tiendas.config(state=DISABLED)
        V_tienda.set("")

    elif V_Opcion.get() == "Movimientos Bancarios Dolares":
        E_Fecha.config(state= "normal")
        E_Tiendas.config(state=DISABLED)
        V_tienda.set("")
    
    elif V_Opcion.get() == "Trabajadores":
        E_Fecha.config(state= "normal")
        E_Tiendas.config(state=DISABLED)
        V_tienda.set("")

    elif V_Opcion.get() == "Tarjetas":
        E_Fecha.config(state= "normal")
        E_Tiendas.config(state=DISABLED)
        V_tienda.set("")

    elif V_Opcion.get() == "Data Miner":
        E_Fecha.config(state= "normal")
        E_Tiendas.config(state="readonly")
    
    else:
        E_Fecha.config(state= DISABLED)
        E_Tiendas.config(state=DISABLED)
        V_tienda.set("")
        V_fecha.set("")

#####################################################################################
#####################################################################################

E_Ep = ttk.Combobox(
    state="readonly",
    values=[
            "Tiendas",
            "Personal",
            "Cargar RC - TC",
            "Data Miner",
            "Notas de Credito",
            "Peya",
            "Tarjetas",
            ],
    width=20,
    textvariable=V_Opcion
    )
E_Ep.bind("<<ComboboxSelected>>", habilitar_fecha)

E_Fecha = Entry(ventana, font=fontStyle, textvariable=V_fecha, state=DISABLED, justify="center", width=12, disabledbackground=color_fondos)

E_Tiendas = ttk.Combobox(
    state=DISABLED,#"readonly"
    values=tiendas,
    width=30,
    textvariable=V_tienda
    )

E_archivo = Entry(ventana, font=fontStyle, textvariable=V_archivo, state=DISABLED, disabledbackground=color_fondos, justify="center", width=59)
B_seleccionar_ubicacion = Button(ventana,text="Elergir Archivo", font=fontStyle,command=seleccionar_archivo,justify=CENTER, background=color_fondos, activebackground=fondo_activo_boton)

B_cargar = Button(ventana,text="Cargar", font=fontStyle,command=cargar,justify=CENTER, width=10, background=color_fondos, activebackground=fondo_activo_boton)
B_actualizar = Button(ventana,text="Actualizar", font=fontStyle,command=actualizar,justify=CENTER, width=10, background=color_fondos, activebackground=fondo_activo_boton)
B_eliminar = Button(ventana, text="Eliminar", font=fontStyle, command=eliminar, justify=CENTER, width=10, background=color_fondos, activebackground=fondo_activo_boton)
#######################################################################################################
#######################################################################################################
canvas.create_text(ventana_ancho/2,5,text="Cargar Datos:", anchor='n', font=fontStyle)

canvas.create_text(20,35,text="Elegir Carga:", anchor='nw', font=fontStyle)
canvas.create_window(110, 33, window=E_Ep, anchor='nw')
canvas.create_window(270, 30, window=B_seleccionar_ubicacion, anchor='nw')

canvas.create_window(16, 67, window=E_archivo, anchor='nw')

canvas.create_text(20,105,text="Fecha:", anchor='nw', font=fontStyle)
canvas.create_window(70, 105, window=E_Fecha, anchor='nw')
canvas.create_text(170,105,text="Tienda:", anchor='nw', font=fontStyle)
canvas.create_window(230, 103, window=E_Tiendas, anchor='nw')

canvas.create_window(60, 140, window=B_cargar, anchor='nw')
canvas.create_window(ventana_ancho/2, 140, window=B_actualizar, anchor='n')
canvas.create_window(390, 140, window=B_eliminar, anchor='ne')

#######################################################################################################

ventana.mainloop()