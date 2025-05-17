#Ejercicio 1
def multiplica_por_2(numero):
    for i in range(numero+1):
        print(i*2)

multiplica_por_2(5)

print("----------------------------")

#Ejercicio 2
def suma_y_resta(lista):
    print(lista[0] + lista[1])
    return(lista[0] - lista[1])

lista_numeros = [5,4]

print(suma_y_resta(lista_numeros))

print("----------------------------")

#Ejercicio 3
def sumatoria_menos_longitud(lista):
    suma = 0
    for i in lista:
        suma += i
    resultado = suma - len(lista)
    return resultado

lista_suma = [1,2,3,4]
print(sumatoria_menos_longitud(lista_suma))

print("----------------------------")

#Ejercicio 4
def valores_multiplicados_segundo(lista):
    nueva_lista = []
    if (len(lista) < 2):
        return nueva_lista
    
    for i in range (len(lista)):
       multiplicacion = lista[i] * lista[1]
       nueva_lista.append(multiplicacion)
    print(len(nueva_lista))
    return nueva_lista

lista_inicial = [3,5,6,7,8]
print(valores_multiplicados_segundo(lista_inicial))

print("----------------------------")

def valor_multiplicado_longitud(valor, longitud):
    lista = []

    for i in range (longitud):
        lista.append(valor*longitud)
    
    return lista

print(valor_multiplicado_longitud(123,5))