from conexion.conexion import conexion_ddbb


def registar_tarjetas(datos):
    try:
        conn = conexion_ddbb()
        cursor = conn.cursor()
        # insert_query  = """
        #     INSERT INTO NIUBIZ_TARJETAS (
        #         id_niubiz, diners, cod_comercio, nombre_comercial, fecha, hora, fecha_abono,
        #         producto, tipo_oper, n_tarjeta, origen_tarjeta, tipo_tarjeta, marca_tarjeta,
        #         moneda, monto, comision_total, comision_gravable, igv, neto_abonar, estado,
        #         id_operacion, terminal, cod_autorizacion, n_ref, n_lote, monto_dcc, dcc,
        #         origen_tarjeta2, tipo_tarjeta2, marca_tarjeta2, tipo_captura, banco_emisor,
        #         nro_cuenta_banco_pagador, banco_pagador, nro_cuotas, transaccion_de_cuotas_sin
        #     ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        # """
        insert_query  = """
            INSERT INTO IZIPAY_TARJETAS (
                id_izipay,cod_comercio,producto,tipo_mov,fecha_proceso,fecha_lote,lote_manual,lote_pos,terminal,voucher,autorizacion,cuotas,tarjeta,
                origen,transaccion,fecha_consumo,hora,importe,status,transacción,otros,comision,comision_afecta,igv,neto_parcial,neto_total,fecha_abono,
                fecha_abono_8dig,observaciones,extracomision,comis_standar,comis_porc,nro_id,tpo_comprob,nro_comprob,tipo_tarjeta,serie_terminal,banco_emisor,
                cuota_sin_interes,entidad,hora_trx,nombre_comercial,dcc,moneda_dcc,arn
            ) VALUES ( ? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,?)
        """
        cursor.execute(insert_query,datos)
        
        cursor.commit()
        return False
    except Exception as e:  # Captura la excepción y muestra el error
        print(f"Error --> {e}")
        return True
    finally:
        cursor.close()
        conn.close()
