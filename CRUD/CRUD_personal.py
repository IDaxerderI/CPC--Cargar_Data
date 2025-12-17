from conexion.conexion import conexion_ddbb

def registrar_personal(datos):
    try:
        conn = conexion_ddbb()
        cursor = conn.cursor()
        insert_query = """
                        INSERT INTO PERSONAL (DNI, NOMBRE, CARGO, SERIE_TIENDA, SUB_AREA, FECHA_ING, FECHA_CESE)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """
        cursor.execute(insert_query,datos)
        
        cursor.commit()
    except Exception as e:
        print(f"Error al ingresar personal {e}")
    finally:
        cursor.close()
        conn.close()

def update_personal(datos):
    try:
        conn = conexion_ddbb()
        cursor = conn.cursor()
        update = """
                update PERSONAL set 
                    NOMBRE = ?,
                    CARGO = ?,
                    SERIE_TIENDA = ?,
                    SUB_AREA = ?,
                    FECHA_ING = ?, 
                    FECHA_CESE = ?
                where DNI = ?
                """
        cursor.execute(update,datos)
        cursor.commit()
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al modificar personal: {e}")
    finally:
        cursor.close()
        conn.close()
