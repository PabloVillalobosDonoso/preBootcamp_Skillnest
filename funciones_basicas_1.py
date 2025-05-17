"""
# 1
def cantidad_de_vocales():
    return 5
print(cantidad_de_vocales()) # Imprime 5

#2
def cantidad_de_glaciares_argentina():
    return 16968
print(cantidad_de_dias_o_meses_o_semanas_en_anio() + cantidad_de_glaciares_argentina()) #Error por definicion

#3
def anio_independencia_chile():
    return 1810
    return 1851
print(anio_independencia_chile()) #Imrpime 1810

#4
def cantidad_de_departamentos_colombia():
    return(32)
    print(33)
print(cantidad_de_departamentos_colombia()) #Imprime 32

#5
def altura_machu_picchu():
    print(2438)
x = altura_machu_picchu()
print(x) #Imprime 2438 y luego nada

#6
def suma(a, b):
    print(a+b)
print(suma(10, 5) + suma(4, 3)) #Imprime ERROR AL NO HABER RETORNO

#7
def concatenar(a, b):
    return str(b) + str(a)
print(concatenar(7, 15)) #Imprime 157

#8
def paises_latinoamerica_o_lenguas_indigenas():
    a = 560
    print(a)
    if a < 180:
        return 33
    else:
        return 46
    return 21
print(paises_latinoamerica_o_lenguas_indigenas()) #Imprime 560 y 46

#9
def cantidad_de_dias_o_meses_o_semanas_en_anio(a, b):
    if a < b:
        return 365
    else:
        return 12
    return 52
print(cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3)) #Imprime 365
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4)) #Imprime 12
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4) + cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3)) #Imprime 377

#10
def sumatoria(a, b):
    return a + b
    return 157
print(sumatoria(3, 4)) #Imprime 7

#11
a = 150
print(a)            #Imprime 150
def funcion():
    a = 350
    print(a)
print(a)            #Imprime 150
funcion()           #Imprime 350
print(a)            #Imprime 150

#12
a = 150
print(a)            #Imprime 150
def funcion():
    a = 350         #Imprime 350
    print(a)
    return a
print(a)            #Imprime 150
funcion()
print(a)            #Imprime 150

#13
a = 150
print(a)            #Imprime 150
def funcion():
    a = 350
    print(a)        #Imprime 350
    return a
print(a)            #Imprime 150
a = funcion()
print(a)            #Imprime 350

#14
def funcion1():
    print(3)
    funcion2()
    print(2)
def funcion2():
    print(1)
funcion1()      #Imprime 3, 1 y 2
"""
#15
def funcion1():
    print(3)
    a = funcion2()
    print(a)
    return 4
def funcion2():
    print(1)
    return 0
b = funcion1()
print(b)            #Imprime 3, 1, 0, 4
