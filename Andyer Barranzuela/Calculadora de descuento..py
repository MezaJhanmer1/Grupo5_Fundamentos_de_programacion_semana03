#'def' define la función reutilizable 'calcular_descuento' con dos parámetros de entrada
def calcular_descuento(precio, porcentaje):
    
    #Calculamos el monto a descontar dividiendo el porcentaje entre 100
    ahorro = precio * (porcentaje / 100)
    
    #Restamos el ahorro al precio original para obtener la cantidad final
    precio_final = precio - ahorro
    
    #'return' realiza un retorno múltiple devolviendo una tupla con ambos resultados
    return precio_final, ahorro

# --- ENTRADA DE DATOS Y LLAMADA ---

# Asignamos los datos de prueba a las variables
precio_original = 80
porcentaje_desc = 40

#Invocamos la función y desempaquetamos los dos valores retornados en dos variables
precio_pagar, monto_ahorrado = calcular_descuento(precio_original, porcentaje_desc)

#Salida de datos formateada para mostrar los resultados en la consola
print(f"Precio original: S/ {precio_original}")
print(f"Ahorro obtenido: S/ {monto_ahorrado}")
print(f"Precio final a pagar: S/ {precio_pagar}")