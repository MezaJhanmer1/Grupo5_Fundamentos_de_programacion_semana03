def calcular_descuento(precio, porc):
    descuento = precio * (porc / 100)
    precio_final = precio - descuento
    return precio_final

# Solicitar Info:
precio_inicial = float(input("Agrega el precio Inicial del Producto: "))
porcent_desc = float(input("Agrega el porcentaje de descuento %: "))

# Precio final y ahorro Sacado
precio_desc = calcular_descuento(precio_inicial, porcent_desc)
ahorro = precio_inicial - precio_desc

# Print
print("   DETALLE DE LA COMPRA   ")
print(f"Precio Inicial:     S/.{precio_inicial:.2f}")
print(f"Descuento Aplicado:   {porcent_desc:.2f}%")
print(f"Ahorro Obtenido:    S/.{ahorro:.2f}")
print(f"Precio Final:       S/.{precio_desc:.2f}")
