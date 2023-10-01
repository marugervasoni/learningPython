#promedios duración
otrosCursosMin = 2.5
otrosCursosMax = 7
otrosCursosPromedio = 4
cursoDalto = 1.5

#promedio de crudos
crudoPromedio = 5
crudoDalto = 3.5


# a) diferencia en porcentaje entre el curso actual y el + rapido; + lento y el promedio.
diferenciaConMin = 100 - (cursoDalto / otrosCursosMin * 100)
    #diferenciaConMax = 100 - (cursoDalto / otrosCursosMax * 100) -> da tanto decimal que modificamos la formula (quitamos la coma y luego la agregamos en forma correcta):
diferenciaConMax = 100 - (cursoDalto * 1000 // otrosCursosMax / 10)
diferenciaConPromedio = 100 - (cursoDalto / otrosCursosPromedio * 100)

print("-------------------")
print("El curso de Dalto dura:")
print(f"- un {diferenciaConMin}% menos que el más rápido")
print(f"- un {diferenciaConMax}% menos que el más lento")
print(f"- un {diferenciaConPromedio}% menos que el promedio")
print("-------------------")

# b) porcentaje de material inservible que se reduce en: el promedio y este curso
tiempoVacioPromedio = 100 - otrosCursosPromedio * 1000 // crudoPromedio / 10
tiempoVacioDalto = 100 - cursoDalto * 1000 // crudoDalto / 10

print(f"Un curso promedio elimina un {tiempoVacioPromedio}% de tiempo vacio")
print(f"El curso de Dalto elimina un {tiempoVacioDalto}% de tiempo vacio")
print("-------------------")

# c) ver 10 hs de este curso a cuantas hs de otros crusos equivale. y al reves?
print(f"ver 10hs de este curso equivale a ver {otrosCursosPromedio *100 // cursoDalto / 10} horas de otros cursos")
print(f"ver 10hs de otros cursos equivale a ver {cursoDalto *100 // otrosCursosPromedio / 10} horas de este curso")
print("-------------------")
