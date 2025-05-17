# Ejercicio 1
for i in range (100):
    print(i+1)

# Ejercicio 2
for i in range (500):
    if (i+1) % 2 == 0:
        print(i+1)

# Ejercicio 3
for i in range (100):
    if (i+1) % 10 == 0:
        print("baby")
    elif (i+1) % 5 == 0:
        print("ice ice")
    else:
        print(i+1)

# Ejercicio 4
suma = 0

for i in range (500000):
    suma+=i

print(suma)

# Ejercicio 5
for i in range(2024,0,-3):
    print(i)

# Ejercicio 6
numInicial = int(input("Ingrese numero inicial: "))
numFinal = int(input("Ingrese numero final: "))
multiplo = int(input("Ingrese multiplo: "))

for i in range(numInicial,numFinal+1):
    if i % multiplo == 0:
        print(i)