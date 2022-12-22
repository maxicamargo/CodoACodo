# Dada el área de un cuadrado (en m2), se pide calcular y mostrar su perímetro. 
# Ejemplo: ingresa 25, deberá mostrar 20

#Entrada 
from math import sqrt


areaCuadrado = float(input("Ingrese el Area de un cuadrado: "))

#Proceso
lado = sqrt(areaCuadrado)
perimetroCuadrado = lado * 4

#Salida
print("Un cuadrado de area {} tiene por perimetro {} dado que su lado es igual a {}".format(areaCuadrado,perimetroCuadrado,lado))