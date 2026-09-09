#Escribe una función llamada calcular_descuento(precio, porcentaje) que reciba el precio original de
#un producto y el porcentaje de descuento, y retorne el precio final después del descuento. Luego
#muestra el ahorro obtenido

def calcular_descuento(precio , porcentaje):
#para calcular el descuento se multiplica el precio por el porcentaje y se divide entre 100    
    descuentos = precio*(porcentaje/100)
    precio_final = precio - descuentos
#El retorno de la función es el precio final y el descuento obtenido            
    return precio_final, descuentos    
#Solicitamos al usuario el precio y el porcentaje de descuento
precio = float(input("Ingrese el precio del producto: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))
#1.Llamamos a la función calcular_descuento y almacenamos los valores retornados en las variables 
# precio_final y ahorro
#2. colocamos la , para que retorne dos valores
precio_final,ahorro = calcular_descuento(precio, porcentaje)
#Mostramos los resultados al usuario
print(f"El precio final después del descuento es: {precio_final}")
print(f"El ahorro obtenido es: {ahorro}")
