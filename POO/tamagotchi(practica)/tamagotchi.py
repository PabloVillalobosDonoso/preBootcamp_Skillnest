class Tamagotchi:
    def __init__(self, nombre, color):  #Puedes colocar valores default para salud, felicidad y energia
        self.nombre = nombre
        self.color = color
        self.salud = 50
        self.felicidad = 60
        self.energia = 100

    #Métodos:
    def jugar(self): #incrementa la felicidad el 10, disminuye la salud en 5
        if self.felicidad <= 90:
            self.felicidad += 10
        self.salud -= 5
        self.energia -= 20
        return self
    def comer(self): #incrementa la felicidad en 5, aumenta la salud en 10
        if self.salud <= 90 :
            self.salud += 10
        if self.felicidad <= 95:
            self.felicidad += 5
        self.energia += 10
        return self
    def curar(self): #incrementa la saludo en 20, disminuye la felicidad en 5
        if self.salud <= 80 :
            self.salud += 10
        self.felicidad -= 5
        self.energia += 5
        return self