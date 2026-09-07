def calcular_descuento(precio, porcentaje):
    ahorro = precio * (porcentaje / 100)
    precio_final = precio - ahorro
    return precio_final, ahorro

# --- Entrada de datos y llamada a la función ---
precio_original = 80
porcentaje_desc = 40

precio_pagar, monto_ahorrado = calcular_descuento(precio_original, porcentaje_desc)

print(f"Precio original: S/ {precio_original}")
print(f"Ahorro obtenido: S/ {monto_ahorrado}")
print(f"Precio final a pagar: S/ {precio_pagar}")