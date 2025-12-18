from conexion.conexion import conexion_ddbb

def todas_tiendas():
    try:
        conn = conexion_ddbb()
        cursor = conn.cursor()
        cursor.execute("SELECT SERIE_TIENDA, NOMBRE FROM TIENDAS WHERE COD_COMERCIO is NOT NULL ORDER BY nombre")
        resultados = cursor.fetchall()
        
        return resultados
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al registrar Nota de Credito: {e}")
    finally:
        cursor.close()
        conn.close()

def serie_cod_comercio(codigo):
    try:
        conn = conexion_ddbb()
        cursor = conn.cursor()
        insert_query = "select SERIE_TIENDA from TIENDAS where COD_COMERCIO = ?"#se cambio cod_comercio por cambio de niubiz a izipay
        cursor.execute(insert_query,(codigo,))
        resultados = cursor.fetchall()
        
        cursor.close()
        conn.close()
        return resultados[0][0]
        
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al consultar serie de tienda: {e}")
        return 0

def update_tienda(datos):
    try:
        conn = conexion_ddbb()
        cursor = conn.cursor()
        insert_query = """
                        update TIENDAS set 
                            COD_COMERCIO = ?,
                            COD_DINERS = ?,
                            NOMBRE = ?,
                            BANCO = ?,
                            MARCA = ?
                        where SERIE_TIENDA = ?
                        """
        cursor.execute(insert_query,datos)
        
        cursor.commit()
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error al actualiza Tienda: {e}")
    finally:
        cursor.close()
        conn.close()
