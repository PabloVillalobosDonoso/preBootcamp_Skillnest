numero1 = 70                            #declaración de variable  int
numero2 = 3.14                          #declaración de variable  float
booleano = False                        #declaración de variable  boolean
cadena = 'Hola Mundo'                   #declaración de variable  string
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate']        #inicialización de lista
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False}    #inicialización de diccionario
frutas = ('guayaba', 'fresa', 'papaya')                                             #inicialización de tupla
print(type(frutas))                             #revisión de tipo -> tupla
print(ingredientes_pastel[2])                   #accesar valor listas
ingredientes_pastel.append('Mantequilla')       #agregar valor al final de la lista
print(persona['nombre'])                        #accesar valor diccionario
persona['nombre'] = 'Kevin'                     #cambiar valor diccionario
persona['color_ojos'] = 'cafe'                  #agregar valor diccionario
print(frutas[2])                                #accesar valor tupla

if numero1 > 45:                                #if
    print("Numero mayor")
else:                                           #else
    print("Numero menor")

if len(cadena) < 5:                             #if
    print("Cadena corta")
elif len(cadena) > 15:                          #else if
    print("Cadena larga")
else:                                           #else
    print("Cadena perfecta")

for x in range(8):                              #inicio 0, fin 7, incremento 1
    print(x)
for x in range(2,8):                            #inicio 2, fin 7, incremento 1
    print(x)
for x in range(2,8,2):                          #inicio 2, fin 6, incremento 2
    print(x)
x = 0                                           #asignacion de valor
while(x < 8):                                   #inicio while -> 0, fin while -> 7
    print(x)
    x += 1                                      #incremento en 1

ingredientes_pastel.pop()                       #borra el ultimo valor de la lista
ingredientes_pastel.pop(1)                      #borrar valor lista en el indice 1

print(persona)                                  #imprime el diccionario de persona
persona.pop('color_ojos')                       #elimina la clave de color_ojos
print(persona)                                  #imprime el diccionario de persona actualizado

for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina':
        continue                                #si el ingrediente es Harina, pasar a la siguente iteracion(continue) 
    print('Después de la primera sentencia')    #si no es harina imprime un mensaje
    if ingrediente == 'Chocolate':              #si el ingrediente es un chocolate se termina el for
        break

def imprime_hola_10_veces():
    for numero in range(10):
        print('Hola')

imprime_hola_10_veces()

def imprime_hola_n_veces(n):            #n es el parametro que recibe la funcion para saber cuantas veces iterara
    for numero in range(n):
        print('Hola')

imprime_hola_n_veces(5)                 #5 es el argumento que necesitara la funcion cuando sea llamada

def imprime_hola_n_o_diez_veces(n = 10):    #aqui n se dejara = 10 en caso ed que no se le pase un numero
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces()
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

# print(numero3)                    #->NameError: name <variable name> is not defined
# numero3 = 86                      #->declaracion de variable
# frutas[0] = 'naranja'             #->change value
# print(persona['hobbies'])         #->KeyError: 'hobbies'
# print(ingredientes_pastel[11])    #->IndexError: list index out of range    
# print(booleano)                   #->no hay error
# frutas.append('manzana')          #->add value, error las tuplas no son mutables
# frutas.pop(1)                     #->delete value error las tuplas no son mutables