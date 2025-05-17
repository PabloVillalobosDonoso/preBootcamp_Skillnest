#FUNCIONES
def calcular_ingresos_totales(lista):
    total = 0
    for i in range (len(lista)):
        total += lista[i]["cantidad"] * lista[i]["precio"]
    print("--------------INGRESOS TOTALES--------------------")
    print("Ingresos totales: $" + str(total))

def llenar_ventas_por_producto(ventas_producto, ventas):
    for i in range (len(ventas)):
        nombre = ventas[i]["producto"]
        try:
            ventas_producto[ventas[i]["producto"]] = ventas[i]["cantidad"] + ventas_producto[nombre]
        except:
            ventas_producto[ventas[i]["producto"]] = ventas[i]["cantidad"]
    print("------------VENTAS POR PRODUCTOS--------------")
    for i in ventas_por_producto:
        print(f"{i}\t{ventas_por_producto[i]}")

def identificar_mas_vendido(productos):
    mas_vendido = []
    cant_ventas = 0
    for i in productos:
        if productos[i] > cant_ventas:
            mas_vendido.clear()
            cant_ventas = productos[i]
            mas_vendido.append(i)
        elif productos[i] == cant_ventas:
            mas_vendido.append(i)
    mas_vendido.append(f"cantidad de ventas: {cant_ventas}")
    return(mas_vendido)

def mostrar_suma_total_producto():
    print("-----------------SUMA DE PRODUCTOS VENDIDOS------------------------")
    for i in ventas_por_producto:
        suma = sumar_unidades_vendidas(i)
        precios_por_producto[i] = (suma,ventas_por_producto[i])
    for i in precios_por_producto:
        print("Cantidad de productos vendidos :", i ,precios_por_producto[i][1])
        print("Precio promedio de ventas : $" + str(precios_por_producto[i][0]/(precios_por_producto[i][1])),"\n")

def sumar_unidades_vendidas(producto):
    suma = 0
    for i in range (len(ventas)):
        if ventas[i]["producto"] == producto:
            suma += ventas[i]["precio"] * ventas[i]["cantidad"]
    return suma

def llenar_ingresos_por_dia():
    print("-------------------INGRESOS POR DIA---------------------")
    for i in range (len(ventas)):
        try:
            ingresos_por_dia[ventas[i]["fecha"]] = (ventas[i]["precio"]*ventas[i]["cantidad"]) + ingresos_por_dia[ventas[i]["fecha"]]
        except:
            ingresos_por_dia[ventas[i]["fecha"]] = (ventas[i]["precio"]*ventas[i]["cantidad"])
    for i in ingresos_por_dia:
        print("Ingresos del día", i,": $" + str(ingresos_por_dia[i]))

def crear_resumen_ventas():
    for i in ventas_por_producto:
        precio_promedio = precios_por_producto[i][0]/(precios_por_producto[i][1])
        resumen_ventas[i] = {"cantidad_total": ventas_por_producto[i], "ingresos_totales": precios_por_producto[i][0], "precio_promedio": precio_promedio}
    print("---------RESUMEN DE VENTAS----------")
    for i in resumen_ventas:
        print(f"{i}\t\t\t Cantidad total: {resumen_ventas[i]["cantidad_total"]}, Total de ingresos: ${resumen_ventas[i]["ingresos_totales"]}, Precio Promedio: ${resumen_ventas[i]["precio_promedio"]}")

#DICCONARIOS
ventas = [
    {"fecha": '2025-03-22', "producto":"Coca-cola", "cantidad":2, "precio":2400.00},
    {"fecha": '2025-05-14', "producto":"Juego ps4", "cantidad":2, "precio":7500.00},
    {"fecha": '2025-05-16', "producto":"Remedios", "cantidad":3, "precio":4990.00},
    {"fecha": '2025-05-13', "producto":"Manga", "cantidad":1, "precio":12990.00},
    {"fecha": '2025-05-05', "producto":"Kem treme", "cantidad":2, "precio":950.00},
    {"fecha": '2025-05-05', "producto":"Cochocolate", "cantidad":2, "precio":1000.00},
    {"fecha": '2025-05-10', "producto":"Pan", "cantidad":9, "precio":250.00},
    {"fecha": '2025-05-14', "producto":"Bidon de agua", "cantidad":1, "precio":4000.00},
    {"fecha": '2025-05-16', "producto":"Leche", "cantidad":2, "precio":1290.00},
    {"fecha": '2025-05-01', "producto":"Cereal", "cantidad":1, "precio":3800.00},
    {"fecha": '2025-05-07', "producto":"Arroz", "cantidad":4, "precio":1790.00},
    {"fecha": '2025-03-22', "producto":"Coca-cola", "cantidad":2, "precio":2400.00},
    {"fecha": '2025-03-22', "producto":"Coca-cola", "cantidad":2, "precio":2400.00},
    {"fecha": '2025-03-22', "producto":"Coca-cola", "cantidad":4, "precio":2400.00},
    {"fecha": '2025-03-22', "producto":"Coca-cola", "cantidad":4, "precio":2400.00},
    {"fecha": '2025-05-16', "producto":"Leche", "cantidad":2, "precio":1290.00},
    {"fecha": '2025-05-14', "producto":"Aceite", "cantidad":6, "precio":2200.00},
    {"fecha": '2025-05-08', "producto":"Helado", "cantidad":2, "precio":1290.00},
    {"fecha": '2025-05-12', "producto":"Leche", "cantidad":3, "precio":1290.00},
    {"fecha": '2025-05-10', "producto":"Doritos", "cantidad":1, "precio":1690.00},
    {"fecha": '2025-05-16', "producto":"Arroz", "cantidad":5, "precio":1790.00},
    {"fecha": '2025-05-08', "producto":"Leche", "cantidad":2, "precio":1290.00},
    {"fecha": '2025-05-11', "producto":"Pan", "cantidad":5, "precio":250.00},
    {"fecha": '2025-05-02', "producto":"Leche", "cantidad":4, "precio":1290.00}
]

ventas_por_producto = {}
precios_por_producto = {}
ingresos_por_dia = {}
resumen_ventas = {}

calcular_ingresos_totales(ventas)
llenar_ventas_por_producto(ventas_por_producto, ventas)
print("---------------PRODUCTOS MAS VENDIDOS---------------")
print("El/los productos más vendido/s es/son:", identificar_mas_vendido(ventas_por_producto))
mostrar_suma_total_producto()
llenar_ingresos_por_dia()
crear_resumen_ventas()