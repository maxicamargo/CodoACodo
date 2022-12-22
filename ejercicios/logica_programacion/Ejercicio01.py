# Dados el valor de una hora de trabajo y la cantidad de horas trabajadas por día, la aplicación 
# muestra el valor del sueldo diario. Ejemplo: si ingresa 400 y 8, mostrará: 3200

#Entrada
sueldo = float(input("Ingrese el valor de la hora de trabajo: "))
horas = int(input("Ingrese la cantidadde horas trabajadas: "))

#Proceso
sueldoDiario = sueldo * horas

#Salida
print("El sueldo diario a cobrar es $ {}".format(sueldoDiario))