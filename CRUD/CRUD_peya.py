from conexion.conexion import conexion_ddbb

def registrar_peya(datos):
    try:
        conn = conexion_ddbb()
        cursor = conn.cursor()
        insert_query = """
                        insert into MOVIMIENTOS_PEYA (
                            ID_PEDIDO,
                            ID_RESTAURANTE,
                            ENTREGA,
                            FORMA_PAGO,
                            ESTADO_PEDIDO,
                            FECHA,
                            HORA,
                            TOTAL,
                            RESARCIMIENTO)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
                        """
        cursor.execute(insert_query,datos)
        
        cursor.commit()
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al registrar Peya: {e}")
    
    finally:
        cursor.close()
        conn.close()
