class Animal:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def hacer_truco(self):
        print(f"{self.nombre} realiza un truco")

    def hacer_sonido(self):
        raise NotImplementedError

class Gato(Animal):
    def __init__(self, nombre, edad, color, tipo_pelaje):
        super().__init__(nombre, edad, color)
        self.tipo_pelaje = tipo_pelaje

    def hacer_truco(self):
        print(f"{self.nombre} te ignora un momento")
        #super().hacer_truco()   #asi se llama una funcion de la clase padre
        print(f"{self.nombre} se rehúsa a hacer el truco")
    
    def hacer_sonido(self):
        print("miiiaaaaauuu")

unicornio = Animal("Azulito", 0, "arcoris")
miu = Gato("Miu", 5, "blanca", "largo")

unicornio.hacer_truco()
miu.hacer_truco()
miu.hacer_sonido()