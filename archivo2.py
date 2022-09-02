class   Vehiculo:
    color = ""
    puertas = 4
    ruedas = 4

    def __init__(self, color, puertas, ruedas) -> None:
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas
        print (str(f"el color del carro es {color}, tiene {puertas} puertas y tiene {ruedas} ruedas"))

mustang = Vehiculo("rojo", 5, 5)

from ast import dump
from pickle import *

archivo = open("carro", "w+b")
dump(mustang, archivo)
archivo.seek(0)
otro_mustang = load(archivo)
archivo.close()