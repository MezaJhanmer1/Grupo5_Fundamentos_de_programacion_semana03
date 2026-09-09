#Crea una función es_par(numero) que retorne True si el número es par o False si es impar. Luego crea otra
#función mostrar_paridad(numero) (sin return) que use la primera función e imprima el resultado en pantalla
#con un mensaje.
#coloca la funcion es_par para determinar si el numero es par o impar y que retorne un valor booleano
def es_par(numero):
    if numero % 2 == 0:
        return "es Par"
    else:
        return "es Impar"
# colocamos la funcion mostrar_paridad que no tiene return y que llama a la funcion es_par para mostrar el resultado
def mostrar_paridad(numero):
    resultado = es_par(numero)
    print(f"El número {numero} {resultado}.")
#Solicitamos al usuario que ingrese un número
numero = int(input("Ingrese un número: "))
mostrar_paridad(numero)

