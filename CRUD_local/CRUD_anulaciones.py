from conexion.conexion import conexion_ddbb_antigua

def cargar(datos):
    
    try:
        conn = conexion_ddbb_antigua()
        cursor = conn.cursor()
        #INSERT INTO DB_ANULACIONES (id ,SERIE ,CORRELATIVO ,TRANSACCION ,FECHA_EMIS ,HORA ,CAJERO ,TOTAL ,NUEV_BOL ,COD_ANULACION ,CERTIFICACION ,HORA_NBV ,MOTIVO ,DESCRIPCION)
        #VALUES (? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,?);
        insert_query = """
                        insert into DB_ANULACIONES (id,SERIE,CORRELATIVO,TRANSACCION,FECHA_EMIS,HORA,CAJERO,TOTAL,NUEV_BOL,COD_ANULACION,CERTIFICACION,HORA_NBV,MOTIVO,DESCRIPCION)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,? );
                        """
        cursor.execute(insert_query,datos)
        
        cursor.commit()
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al registrar anulacion: {e}")
    finally:
        cursor.close()
        conn.close()


def actualizar(datos):
    
    try:
        conn = conexion_ddbb_antigua()
        cursor = conn.cursor()
        #INSERT INTO DB_ANULACIONES (id ,SERIE ,CORRELATIVO ,TRANSACCION ,FECHA_EMIS ,HORA ,CAJERO ,TOTAL ,NUEV_BOL ,COD_ANULACION ,CERTIFICACION ,HORA_NBV ,MOTIVO ,DESCRIPCION)
        #VALUES (? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,?);
        insert_query = """
                        update DB_ANULACIONES set
                            SERIE = ?,
                            CORRELATIVO = ?,
                            TRANSACCION = ?,
                            FECHA_EMIS = ?,
                            HORA = ?,
                            CAJERO = ?,
                            TOTAL = ?,
                            NUEV_BOL = ?,
                            COD_ANULACION = ?,
                            CERTIFICACION = ?,
                            HORA_NBV = ?,
                            MOTIVO = ?,
                            DESCRIPCION = ?
                        where ID = ?
                        """
        cursor.execute(insert_query,datos)
        
        cursor.commit()
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al actualizar anulacion: {e}")
    finally:
        cursor.close()
        conn.close()