# Función modular: recibe la lista de notas por referencia (sin modificarla)
def calcular_promedio(notas):
    # Funciones built-in: sum() suma los elementos y len() los cuenta para hallar el promedio
    promedio = sum(notas) / len(notas)
    
    # min() busca la nota más baja y max() la más alta dentro de la lista
    nota_min = min(notas)
    nota_max = max(notas)
    
    # Retorno múltiple: empaqueta los tres resultados en una tupla y los devuelve
    return promedio, nota_min, nota_max

# Función de procedimiento (void): no usa 'return', solo le da formato a los datos para imprimirlos
def mostrar_resultado(nombre, notas):
    # Desempaquetado: llama a la primera función y guarda los 3 valores de la tupla en variables
    prom, mn, mx = calcular_promedio(notas)
    
    # Salida de datos en consola con cadenas formateadas (f-strings)
    print(f"--- REPORTE DE: {nombre} ---")
    print(f"Promedio: {prom:.2f}")  # ':2f' redondea la salida a dos decimales
    print(f"Nota mínima: {mn}")
    print(f"Nota máxima: {mx}")

# --- BLOQUE DE EJECUCIÓN ---

# Definimos la lista de notas que le pasaremos al programa
mis_notas = [16, 18, 14, 20]

# Invocamos la función de procedimiento pasando el nombre "Andyer" y la lista de notas
mostrar_resultado("Andyer", mis_notas)