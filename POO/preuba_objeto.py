class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def getName(self):
        return(self.nombre)
    
    def cumple(self):
        self.edad += 1