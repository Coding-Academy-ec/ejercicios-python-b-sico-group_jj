
# 1 Escribe un programa en Python que imprima tu nombre en la pantalla.
def imprimir_nombre():
#    print("Javier Eduardor Jordan")
    print("Diego F. Tandazo Yaguachi")

if __name__ == "__main__":
    imprimir_nombre()

# 2 Escribe un programa que calcule la suma de los números del 1 al 10.
def suma_1_al_10():
    suma = sum(range(1, 11))  # Se utiliza la función sum() para calcular la suma del rango del 1 al 10
    return suma

if __name__ == "__main__":
    resultado = suma_1_al_10()  # Se llama a la función suma_1_al_10() para obtener el resultado
    print ("El resultado es " , resultado)

# 3 Crea variables para almacenar tu edad, nombre y estatura, e imprímelas en pantalla.
def imprimir_datos_personales(nombre, edad, estatura):
    print("Nombre:", nombre,"\nEdad:", edad,"\nEstatura:",estatura)

if __name__ == "__main__":
    # Se definen las variables con los datos personales
    nombre="Diego"
    edad=32
    estatura=1.69
    imprimir_datos_personales(nombre,edad,estatura)

# 4 Escribe un programa que determine si un número ingresado por el usuario es par o impar.
def par_o_impar(numero):
    if numero % 2 == 0 :
        return "par"
    else:
        return "impar"

if __name__ == "__main__":
    num = int(input("Ingrese un número para validar si es o no Par: "))  # Se solicita al usuario que ingrese un número
    print(par_o_impar(num))  # Se imprime si el número ingresado es par o impar

# 5 Crea una función que calcule el área de un círculo dado su radio.
import math

def area_circulo(radio):
    area = math.pi * radio ** 2  # Se calcula el área del círculo utilizando la fórmula matemática
    return area

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))  # Se solicita al usuario que ingrese el radio del círculo
    print("EL AREA ES ", area_circulo(radio) )

# 6 Define una función que reciba dos números como argumentos y devuelva su suma.
def suma(a, b):
    return a + b

if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))  # Se solicita al usuario que ingrese el primer número
    num2 = int(input("Ingrese el segundo número: ")) 
    print("La suma es:", suma(num1, num2))  # Se imprime la suma de los dos números ingresados

# 7 Modifica la función que calcula el área del círculo para que reciba el radio como parámetro.
import math

def area_circulo(radio):
    area = math.pi * radio ** 2  # Se calcula el área del círculo utilizando la fórmula matemática
    return area # Se devuelve el área calculada

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))  # Se solicita al usuario que ingrese el radio del círculo
    print("El área del círculo es:", area_circulo(radio))  # Se imprime el área calculada del círculo

# 8 Diseña un programa que convierta grados Celsius a Fahrenheit y viceversa, utilizando funciones para realizar los cálculos.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32  # Se aplica la fórmula de conversión de Celsius a Fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit -32 ) * 5/9
    

if __name__ == "__main__":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))  # Se solicita al usuario que ingrese la temperatura en grados Celsius
    print("Temperatura en Fahrenheit:", celsius_a_fahrenheit(celsius))  # Se imprime la temperatura convertida a grados Fahrenheit
    # Se solicita al usuario que ingrese la temperatura en grados Fahrenheit
    fahrenheit = float(input("Ingrese la temperatura en grados fahrenheit: ")) 
    print("Temperatura en Celsius:", fahrenheit_a_celsius(fahrenheit))  # Se imprime la temperatura convertida a grados Celsius
