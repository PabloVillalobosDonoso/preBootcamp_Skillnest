from tamagotchi import Tamagotchi

class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    #Métodos:
    def jugar_con_tamagotchi(self): #juega e invoca el método de tamagotchi jugar()
        print(f"{self.nombre} está juagnado con {self.tamagotchi.nombre}!!")
        self.tamagotchi.jugar()
        return self
    def darle_comida(self): #le da de comer su tamagotchi invocando al método de tamagotchi comer()
        print(f"{self.nombre} está alimentanto a {self.tamagotchi.nombre} >.<")
        self.tamagotchi.comer()
        return self
    def curarlo(self): #sana las heridas de su tamagotchi invocando al método de tamagotchi curar()
        print(f"{self.nombre} está curando a {self.tamagotchi.nombre} OwO")
        self.tamagotchi.curar()
        return self

alex = Tamagotchi("Alex","rojo")
jugador = Persona("Pablo", "Villalobos",alex)

jugador.jugar_con_tamagotchi()
jugador.darle_comida()
jugador.curarlo()