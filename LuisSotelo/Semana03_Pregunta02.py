#funcion par
def es_par(numero):
    return numero % 2 == 0

#Print si es par o impar
def mostrar_paridad(numero):
    if es_par(numero):
        print(f"El número {numero} es PAR.")
    else:
        print(f"El número {numero} es IMPAR.")

# Prueba
mostrar_paridad(10)   
mostrar_paridad(55)  
mostrar_paridad(0)   