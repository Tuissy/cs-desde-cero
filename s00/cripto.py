def mejor_operacion(precios):
    for i in range(len(precios)):
        try:
            precio_minimo = min(precios)
            indice_minimo = precios.index(precio_minimo)
            dia_compra = indice_minimo + 1

            precio_max = max(precios[dia_compra :])
            indice_max = precios.index(precio_max)
            dia_venta = indice_max + 1
        except ValueError:
            return None
        
        ganancia = precio_max - precio_minimo
        if ganancia <= 0:    
            return None
        
        return dia_compra, dia_venta, ganancia

print(mejor_operacion([6,1,6]))
