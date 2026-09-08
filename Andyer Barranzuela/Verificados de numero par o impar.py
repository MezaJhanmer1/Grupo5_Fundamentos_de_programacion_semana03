# Función lógica: devuelve 'True' o 'False' según la condición
def es_par(numero):
    # El operador '%' calcula el residuo; si dividir entre 2 da residuo 0, es True
    return numero % 2 == 0

# Función de procedimiento (tipo void): no usa 'return', solo imprime la salida
def mostrar_paridad(numero):
    # Composición de funciones: evalúa la respuesta de 'es_par' en el condicional 'if'
    if es_par(numero):
        # Si la respuesta es True, imprime que el número es PAR
        print(f"El número {numero} es PAR")
    else:
        # Si la respuesta es False, imprime que el número es IMPAR
        print(f"El número {numero} es IMPAR")

# --- BLOQUE DE EJECUCIÓN ---

# Definimos la lista de números que vamos a evaluar
numeros = [5, 9, 130, 150]

# Bucle 'for': pasa cada número de la lista uno por uno a la función de procedimiento
for num in numeros:
    mostrar_paridad(num)