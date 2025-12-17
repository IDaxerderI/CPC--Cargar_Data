from datetime import datetime

def validar_fecha(fecha_ing):
    try:
        fecha = datetime.strptime(fecha_ing,"%d/%m/%y").date()
    except:
        pass
    
    try:
        fecha = datetime.strptime(fecha_ing,"%Y-%m-%d").date()
    except:
        pass
    
    try:
        fecha = datetime.strptime(fecha_ing,"%d/%m/%Y").date()
    except:
        pass
    
    return fecha