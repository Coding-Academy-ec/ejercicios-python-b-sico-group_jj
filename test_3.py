from programa import imprimir_datos_personales
from io import StringIO
import sys

def test_imprimir_datos_personales(capsys):
#    nombre = "Javier"
#    edad = 30
#    estatura = 1.75
    nombre="Diego"
    edad=32
    estatura=1.69
    imprimir_datos_personales(nombre, edad, estatura)
    captured = capsys.readouterr()
#    assert captured.out == "Nombre:Javier\nEdad:30\nEstatura:1.75\n"
    assert captured.out == "Nombre: Diego \nEdad: 32 \nEstatura: 1.69\n"