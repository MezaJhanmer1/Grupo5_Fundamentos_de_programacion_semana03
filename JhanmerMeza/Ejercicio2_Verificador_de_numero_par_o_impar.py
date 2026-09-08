#Comenzamos definiendo nuestra funcion es_par que recibira un numero y verificara si es par
def es_par(numero):
    #Si el residuo es 0 la comparación devuelve True automáticamente en ese caso el numero es par
    return numero % 2 == 0

#Con esta funcion mostraremos en pantalla si el numero ingresado es par o impar
def mostrar_paridad(numero):

    #se evalua la funcion es_par (el booleano que devuelve la función), la estructura del if evalua lo que tiene al lado si es false o true
    if es_par(numero):
        print(f"El numero {numero} es par ")

    else:
        print(f"El numero {numero} es impar ")

n1= int(input("Ingrese un numero para verificar si es par o impar: "))

mostrar_paridad(n1)


