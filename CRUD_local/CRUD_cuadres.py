from conexion.conexion import conexion_ddbb

def cargar(datos):
    
    try:
        conn = conexion_ddbb()
        cursor = conn.cursor()
        #INSERT INTO DB_ANULACIONES (id ,SERIE ,CORRELATIVO ,TRANSACCION ,FECHA_EMIS ,HORA ,CAJERO ,TOTAL ,NUEV_BOL ,COD_ANULACION ,CERTIFICACION ,HORA_NBV ,MOTIVO ,DESCRIPCION)
        #VALUES (? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,?);
        insert_query = """
                        insert into CUADRES (FECHA,SERIE_TIENDA,DNI_ADMIN,DNI_CAJERO,TURNO,N_CAJA,EFECTIVO_SOL,EFECTIVO_DOL,TARJETA_LUCHA,VISA,DINERS,AMEX,QR,PEYA_WEB,PEYA_35,PIXEL_EFECTIVO,PIXEL_T_LUCHA,PIXEL_TARJETA,PIXEL_PEYA,FAT_CAJA,SOB_CAJ,CAJA,OBS,DNI_DSCT)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
                        """
        cursor.execute(insert_query,datos)
        
        cursor.commit()
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al registrar Cuadre: {e}")
    finally:
        cursor.close()
        conn.close()