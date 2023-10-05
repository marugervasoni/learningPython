# a) pedir al usuario que diga un texto real y calcular cuanto tardaría en decir esa frase - cuantas palabras dijo
texto = input("Decime una frase y calculo cuanto tardas en decirla: ")
palabrasSeparadas = texto.split(" ")
cantidadPalabras = len(palabrasSeparadas)

print(f"Dijiste {cantidadPalabras} palabras, y tardarías {cantidadPalabras/2} segundos en decirlo")


# b) si tarda + de 1 minuto, decirle "para flaco tampoco te pedí un testamento"
if cantidadPalabras > 120:
    print("para flaco, tampoco te pedi un testamento")


# c) dalto habla un 30% + rapido -cuanto tardaría el en decirlo
print(f"Dalto lo diría en {round(cantidadPalabras/2 /1.3,2)} segundos en decirlo")