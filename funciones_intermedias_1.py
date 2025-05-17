#Ejercicio 1
print("-----------------Ejercicio 1-----------------------")
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

matriz[1][0] = 6
print(matriz)

cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)

ciudades["México"][2] = "Monterrey"
print(ciudades)

coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

#Ejercicio 2
print("-----------------Ejercicio 2-----------------------")

def iterarDiccionario(lista):
    for i in range (len(lista)):
        print("nombre - " + lista[i]["nombre"] + " pais - " + lista[i]["pais"])

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)

print("-----------------Ejercicio 3-----------------------")
#Ejercicio 3

def iterarDiccionario2(llave, lista):
    for i in range (len(lista)):
        print(lista[i][llave])

iterarDiccionario2("nombre", cantantes)
iterarDiccionario2("pais", cantantes)

print("-----------------Ejercicio 4-----------------------")
#Ejercicio 4

def imprimirInformacion(diccionario):
    for i in diccionario:
        print(len(diccionario[i]), i.upper())
        for j in range(len(diccionario[i])):
            print(diccionario[i][j])
        print()

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)