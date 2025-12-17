from conexion.conexion import conexion_ddbb_antigua

def cargar(datos):
    
    try:
        conn = conexion_ddbb_antigua()
        cursor = conn.cursor()
        #INSERT INTO DB_ANULACIONES (id ,SERIE ,CORRELATIVO ,TRANSACCION ,FECHA_EMIS ,HORA ,CAJERO ,TOTAL ,NUEV_BOL ,COD_ANULACION ,CERTIFICACION ,HORA_NBV ,MOTIVO ,DESCRIPCION)
        #VALUES (? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,?);
        insert_query = """
                        insert into CUADRES (SERIE_TIENDA,FECHA,FECHA_ABONO,N_OPERACION,ABONO,BANCO,TIPO_MONEDA)
                        VALUES (?,?,?,?,?,?,?);
                        """
        cursor.execute(insert_query,datos)
        
        cursor.commit()
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al registrar Movimientos: {e}")
    finally:
        cursor.close()
        conn.close()