from conexion.conexion import conexion_sql, conexion_ddbb

def registrar_nc(datos):
    try:
        conn = conexion_ddbb()
        cursor = conn.cursor()
        #INSERT INTO DB_ANULACIONES (id ,SERIE ,CORRELATIVO ,TRANSACCION ,FECHA_EMIS ,HORA ,CAJERO ,TOTAL ,NUEV_BOL ,COD_ANULACION ,CERTIFICACION ,HORA_NBV ,MOTIVO ,DESCRIPCION)
        #VALUES (? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,?);
        insert_query = """
                        INSERT INTO DB_ANULACIONES (id ,SERIE ,CORRELATIVO ,TRANSACCION ,FECHA_EMIS ,HORA ,CAJERO ,TOTAL)
                        VALUES (? ,? ,? ,? ,? ,? ,? ,?);
                        """
        cursor.execute(insert_query,datos)
        
        cursor.commit()
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al registrar Nota de Credito: {e}")
        print(f"Datos --> {datos}")
    finally:
        cursor.close()
        conn.close()
    
def todas_trans(fecha, fecha_limite):
    c_serie = "%C%%"
    try:
        conn = conexion_sql()
        cursor = conn.cursor()
        
        consulta = """SELECT serie, CORRELATIVO, TRANSACCION, FECH_EMIS, HORA, CAJERO, MONT_TOTA  
                        FROM DIGICOMPROBANTES 
                        where serie like ? and 
                        FECH_EMIS between ? and ?"""
        cursor.execute(consulta,(c_serie, fecha, fecha_limite))
        
        resultados = cursor.fetchall()
        
        return resultados
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al elegir Transaccion: {e}")
    finally:
        cursor.close()
        conn.close()