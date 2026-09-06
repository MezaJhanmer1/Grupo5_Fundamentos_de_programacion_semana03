print("Bienvenido a la calculadora de descuentos a continuacion ingrese los valores:")
print("------------------------------------------------------------------------------")
# Primero pedimos al usuario el precio incial del producto
precio_inicial = float(input("Ingresa el precio del producto: "))

# Luego pedimos el porcentaje de descuento
porcentaje_de_descuento = float(input("Ingresa el porcentaje de descuento: "))

# Creamos la función que se va calcular el precio final
#Los parametros son el precio y el porcentaje
def calcular_descuento(precio,porcentaje):

    # Calculamos cuánto dinero representa el descuento
    descuento = precio * (porcentaje/100)

    # Al precio original le restamos el descuento para saber cuanto es lo que se pagara
    
    precio_final = precio - descuento

    # La función return devuelve el precio final
    return precio_final

# Llamamos a la función y guardamos el resultado en la variable "luego del descuento"
luego_del_descuento = calcular_descuento(precio_inicial,porcentaje_de_descuento)

# Para saber cuánto dinero ahorramos restamos el precio final al precio inicial.
ahorro = precio_inicial - luego_del_descuento


print("El precio final es: ", luego_del_descuento)
print ("Este es el monto que ahorraste con esta compra: ",ahorro )