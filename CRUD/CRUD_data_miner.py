from conexion.conexion import conexion_sql, conexion_ddbb

def consulta_vta_diaria(fecha,serie):
    try:
        conn = conexion_sql()
        cursor = conn.cursor()
        
        consulta = f"""ventaCajas '{fecha}','{serie}'"""
        cursor.execute(consulta)
        
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al elegir Comprobante: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def registrar_data_miner(datos):
    try:
        conn = conexion_ddbb()
        cursor = conn.cursor()
        #INSERT INTO DB_ANULACIONES (id ,SERIE ,CORRELATIVO ,TRANSACCION ,FECHA_EMIS ,HORA ,CAJERO ,TOTAL ,NUEV_BOL ,COD_ANULACION ,CERTIFICACION ,HORA_NBV ,MOTIVO ,DESCRIPCION)
        #VALUES (? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,?);
        insert_query = """
                        INSERT INTO DATA_MINER (CAJERO,TRANSACCION,NETO,TOTAL,SERIE_TIENDA,FECHA)
                        VALUES (? ,? ,? ,? ,? ,? );
                        """
        cursor.execute(insert_query,datos)
        
        cursor.commit()
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al registrar data miner local: {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_data_miner_dia(dia,serie):
    try:
        conn = conexion_ddbb()
        cursor = conn.cursor()
        insert_query ="delete from DATA_MINER where FECHA=? and SERIE_TIENDA = ?"
        cursor.execute(insert_query,(dia,serie))
        
        cursor.commit()
        
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al eliminar DATA_MINER: {e}")
    finally:
        cursor.close()
        conn.close()