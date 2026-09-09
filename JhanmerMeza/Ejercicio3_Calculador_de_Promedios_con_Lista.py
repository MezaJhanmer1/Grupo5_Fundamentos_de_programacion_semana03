#calcula el promedio, la nota mínima y la nota máxima
def calcular_promedio(notas):
    #sum(notas) suma todas las notas
    # len(notas) cuenta cuántas notas hay
    promedio = sum(notas) / len(notas)
    # min() busca la nota más pequeña de la lista
    minima = min(notas)
    # max() busca la nota más grande de la lista
    maxima = max(notas)
    # La función devuelve los tres resultados
    return promedio,minima,maxima
# Esta función muestra el reporte en pantalla.
def mostrar_resultado(nombre, notas):

 # Llamamos a calcular_promedio() y recibimos sus tres resultados.
    prome,mn,mx = calcular_promedio(notas)

    print("\n ---------- Reporte de Notas -------------")
    print(f"Nombre: {nombre}")
    print(f"Notas: {notas}")
    
    # "":.2f" significa que mostramos el promedio con 2 números después del punto decimal.
    print(f"Promedio: {prome: .2f}")
    print(f"Nota minima: {mn}")
    print(f"Nota maxima: {mx}")

nombre = input("Ingresa el nombre del estudiante: ")

cantidad = int(input("¿Cuantas notas desea ingresar?: "))

# Creamos una lista vacía donde guardaremos las notas.
notas = []
# Este ciclo se repite según la cantidad de notas indicada.
for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i + 1}: "))

     # Agregamos las notas ingresadas a la lista notas que estaba vacia.
    notas.append(nota)  
# Finalmente llamamos a la función que muestra el reporte.
mostrar_resultado(nombre, notas)                