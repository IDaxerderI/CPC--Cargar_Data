from conexion.conexion import conexion_ddbb

def registrar_TC_RC(datos):
    try:
        conn = conexion_ddbb()
        cursor = conn.cursor()
        insert_query = """
                        INSERT INTO TC_RC (FECHA,TIPO_CAMBIO,RECARGO)
                        VALUES (? ,? ,?);
                        """
        cursor.execute(insert_query,datos)
        
        cursor.commit()
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al registrar Tipo de cambio y recargo: {e}")
    finally:
        cursor.close()
        conn.close()

def actualizar_TC_RC(datos):
    try:
        conn = conexion_ddbb()
        cursor = conn.cursor()
        insert_query = """
                        update TC_RC set 
                            TIPO_CAMBIO = ?,
                            RECARGO = ?
                        where FECHA = ?
                        """
        cursor.execute(insert_query,datos)
        
        cursor.commit()
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al actualizar Tipo de cambio y recargo: {e}")
    finally:
        cursor.close()
        conn.close()